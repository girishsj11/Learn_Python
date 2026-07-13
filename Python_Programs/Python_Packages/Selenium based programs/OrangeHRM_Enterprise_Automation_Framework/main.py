"""Local entry point for the OrangeHRM UI suite."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime
from html import escape
from pathlib import Path
import sys

import pytest


ROOT_DIR = Path(__file__).resolve().parent
TESTS_DIR = ROOT_DIR / "tests"
REPORTS_DIR = ROOT_DIR / "reports"
REPORT_PATH = REPORTS_DIR / "test_report.html"


@dataclass
class CaseResult:
    file_name: str
    nodeid: str
    outcome: str
    duration: float
    details: str = ""
    screenshot: str | None = None


@dataclass
class FileRunResult:
    file_name: str
    exit_code: int


class SequentialResultCollector:
    def __init__(self) -> None:
        self.case_results: list[CaseResult] = []

    def pytest_runtest_logreport(self, report: pytest.TestReport) -> None:
        if report.when not in {"call", "setup"}:
            return

        if report.when == "setup" and not report.skipped:
            return

        self.case_results.append(
            CaseResult(
                file_name=Path(report.location[0]).name,
                nodeid=report.nodeid,
                outcome=report.outcome,
                duration=report.duration,
                details=_format_longrepr(report),
                screenshot=_extract_screenshot(report),
            )
        )


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run OrangeHRM tests by mode")
    parser.add_argument(
        "--mode",
        choices=["ui", "api", "all"],
        help="Choose which test mode to run",
    )
    args, pytest_args = parser.parse_known_args(argv)
    args.pytest_args = pytest_args
    return args


def _prompt_mode() -> str:
    selected = input("Run tests in which mode? [ui/api/all] (default: ui): ").strip().lower()
    if selected in {"ui", "api", "all"}:
        return selected
    return "ui"


def _discover_test_files(mode: str) -> list[Path]:
    return sorted(
        path
        for path in TESTS_DIR.glob("test_*.py")
        if path.is_file() and _test_file_matches_mode(path, mode)
    )


def _test_file_matches_mode(test_file: Path, mode: str) -> bool:
    if mode == "all":
        return True

    file_text = test_file.read_text(encoding="utf-8")
    if mode == "ui":
        return "pytest.mark.ui" in file_text
    if mode == "api":
        return "pytest.mark.api" in file_text
    return False


def _format_longrepr(report: pytest.TestReport) -> str:
    if report.passed:
        return ""

    longrepr = report.longrepr
    if hasattr(longrepr, "reprcrash") and longrepr.reprcrash is not None:
        return str(longrepr.reprcrash.message)
    return str(longrepr)


def _extract_screenshot(report: pytest.TestReport) -> str | None:
    for section_name, section_value in getattr(report, "sections", []):
        if section_name == "screenshot":
            screenshot_path = Path(section_value)
            try:
                return screenshot_path.relative_to(REPORTS_DIR).as_posix()
            except ValueError:
                return screenshot_path.as_posix()
    return None


def _scenario_from_file_name(file_name: str) -> str:
    lowered = file_name.lower()
    if "positive" in lowered:
        return "Positive (+ve)"
    if "negative" in lowered:
        return "Negative (-ve)"
    if "edge" in lowered:
        return "Edge"
    if "api" in lowered:
        return "API"
    if "dashboard" in lowered:
        return "Dashboard"
    if "page" in lowered:
        return "Page Object"
    return "General"


def _write_combined_html_report(
    collector: SequentialResultCollector,
    file_runs: list[FileRunResult],
    started_at: datetime,
    finished_at: datetime,
) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    total = len(collector.case_results)
    passed = sum(1 for result in collector.case_results if result.outcome == "passed")
    failed = sum(1 for result in collector.case_results if result.outcome == "failed")
    skipped = sum(1 for result in collector.case_results if result.outcome == "skipped")

    file_rows = []
    for file_run in file_runs:
        file_results = [result for result in collector.case_results if result.file_name == file_run.file_name]
        file_rows.append(
            """
            <tr>
                <td>{scenario}</td>
                <td>{file_name}</td>
                <td>{count}</td>
                <td>{passed}</td>
                <td>{failed}</td>
                <td>{skipped}</td>
            </tr>
            """.format(
                scenario=escape(_scenario_from_file_name(file_run.file_name)),
                file_name=escape(file_run.file_name),
                count=len(file_results),
                passed=sum(1 for result in file_results if result.outcome == "passed"),
                failed=sum(1 for result in file_results if result.outcome == "failed"),
                skipped=sum(1 for result in file_results if result.outcome == "skipped"),
            )
        )

    case_rows = []
    for result in collector.case_results:
        details = escape(result.details) if result.details else ""
        screenshot = f'<a href="{escape(result.screenshot)}">screenshot</a>' if result.screenshot else ""
        case_rows.append(
            """
            <tr class="{status_class}">
                <td>{scenario}</td>
                <td>{file_name}</td>
                <td>{nodeid}</td>
                <td>{outcome}</td>
                <td>{duration:.3f}s</td>
                <td><pre>{details}</pre></td>
                <td>{screenshot}</td>
            </tr>
            """.format(
                status_class=escape(result.outcome),
                scenario=escape(_scenario_from_file_name(result.file_name)),
                file_name=escape(result.file_name),
                nodeid=escape(result.nodeid),
                outcome=escape(result.outcome.upper()),
                duration=result.duration,
                details=details,
                screenshot=screenshot,
            )
        )

    report_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>OrangeHRM Test Report</title>
    <style>
        body {{ font-family: Segoe UI, Arial, sans-serif; margin: 24px; color: #1f2937; }}
        h1, h2 {{ margin-bottom: 12px; }}
        .summary {{ display: grid; grid-template-columns: repeat(4, minmax(120px, 1fr)); gap: 12px; margin: 20px 0; }}
        .card {{ border: 1px solid #d1d5db; border-radius: 8px; padding: 16px; background: #f9fafb; }}
        .passed {{ background: #ecfdf5; }}
        .failed {{ background: #fef2f2; }}
        .skipped {{ background: #fffbeb; }}
        table {{ border-collapse: collapse; width: 100%; margin-bottom: 24px; }}
        th, td {{ border: 1px solid #d1d5db; padding: 10px; text-align: left; vertical-align: top; }}
        th {{ background: #f3f4f6; }}
        pre {{ white-space: pre-wrap; margin: 0; font-family: Consolas, monospace; }}
    </style>
</head>
<body>
    <h1>OrangeHRM Sequential Test Report</h1>
    <p>Started: {started_at}</p>
    <p>Finished: {finished_at}</p>
    <div class="summary">
        <div class="card"><strong>Total</strong><div>{total}</div></div>
        <div class="card passed"><strong>Passed</strong><div>{passed}</div></div>
        <div class="card failed"><strong>Failed</strong><div>{failed}</div></div>
        <div class="card skipped"><strong>Skipped</strong><div>{skipped}</div></div>
    </div>
    <h2>File Summary</h2>
    <table>
        <thead>
            <tr>
                <th>Scenario</th>
                <th>Test File</th>
                <th>Cases</th>
                <th>Passed</th>
                <th>Failed</th>
                <th>Skipped</th>
            </tr>
        </thead>
        <tbody>
            {file_rows}
        </tbody>
    </table>
    <h2>Case Results</h2>
    <table>
        <thead>
            <tr>
                <th>Scenario</th>
                <th>Test File</th>
                <th>Case</th>
                <th>Status</th>
                <th>Duration</th>
                <th>Details</th>
                <th>Artifact</th>
            </tr>
        </thead>
        <tbody>
            {case_rows}
        </tbody>
    </table>
</body>
</html>
""".format(
        started_at=escape(started_at.strftime("%Y-%m-%d %H:%M:%S")),
        finished_at=escape(finished_at.strftime("%Y-%m-%d %H:%M:%S")),
        total=total,
        passed=passed,
        failed=failed,
        skipped=skipped,
        file_rows="\n".join(file_rows),
        case_rows="\n".join(case_rows),
    )

    REPORT_PATH.write_text(report_html, encoding="utf-8")


def run_sequential_suite(mode: str, pytest_args: list[str] | None = None) -> int:
    collector = SequentialResultCollector()
    file_runs: list[FileRunResult] = []
    started_at = datetime.now()
    extra_args = pytest_args or []

    for test_file in _discover_test_files(mode):
        print(f"Running {test_file.relative_to(ROOT_DIR).as_posix()}")
        raw_exit_code = pytest.main(
            [str(test_file), "--mode", mode, "-o", "addopts=-ra", *extra_args],
            plugins=[collector],
        )
        exit_code = int(raw_exit_code)
        if exit_code == int(pytest.ExitCode.NO_TESTS_COLLECTED):
            exit_code = 0
        file_runs.append(FileRunResult(file_name=test_file.name, exit_code=exit_code))

    _write_combined_html_report(collector, file_runs, started_at, datetime.now())
    print(f"Combined HTML report written to {REPORT_PATH}")

    return 1 if any(file_run.exit_code != 0 for file_run in file_runs) else 0


def main() -> int:
    args = _parse_args(sys.argv[1:])

    mode = args.mode
    if mode is None:
        if sys.stdin is not None and sys.stdin.isatty():
            mode = _prompt_mode()
        else:
            mode = "ui"

    return run_sequential_suite(mode, args.pytest_args)


if __name__ == "__main__":
    sys.exit(main())