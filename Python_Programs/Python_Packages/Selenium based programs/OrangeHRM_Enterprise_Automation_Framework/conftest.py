"""Pytest fixtures for the OrangeHRM automation framework."""

from __future__ import annotations

import logging
from logging import FileHandler
import sys
from pathlib import Path

import pytest

from config.env import get_base_url, load_config
from core.browser_factory import create_driver
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utilities.helpers import sanitize_filename
from utilities.screenshot import save_screenshot


ROOT_DIR = Path(__file__).resolve().parent
REPORTS_DIR = ROOT_DIR / "reports"
SCREENSHOTS_DIR = REPORTS_DIR / "screenshots"
LOGS_DIR = ROOT_DIR / "logs"
RUN_LOGGER = logging.getLogger("testrun")
LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
TEST_FILE_LOGGERS: dict[str, logging.Logger] = {}


def _prompt_test_mode() -> str:
    valid_modes = {"ui", "api", "all"}
    prompt = "Select test mode [ui/api/all] (default: ui): "
    selected = input(prompt).strip().lower()
    if selected in valid_modes:
        return selected
    return "ui"


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--mode",
        action="store",
        default=None,
        choices=["ui", "api", "all"],
        help="Run tests by mode: ui, api, or all",
    )


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config: pytest.Config) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    LOGS_DIR.mkdir(parents=True, exist_ok=True)

    config.addinivalue_line("markers", "ui: UI tests that use Selenium")
    config.addinivalue_line("markers", "api: API tests that use HTTP requests")


def pytest_sessionstart(session: pytest.Session) -> None:
    RUN_LOGGER.info("Starting pytest session in %s", ROOT_DIR)


def pytest_runtest_logstart(nodeid: str, location: tuple[str, int, str]) -> None:
    _get_test_file_logger(location[0]).info("START %s", nodeid)
    RUN_LOGGER.info("START %s", nodeid)


def pytest_runtest_logreport(report: pytest.TestReport) -> None:
    if report.when not in {"call", "setup"}:
        return

    if report.when == "setup" and not report.skipped:
        return

    test_logger = _get_test_file_logger(report.location[0])

    if report.passed:
        test_logger.info("PASS %s", report.nodeid)
        RUN_LOGGER.info("PASS %s", report.nodeid)
    elif report.failed:
        test_logger.error("FAIL %s", report.nodeid)
        RUN_LOGGER.error("FAIL %s", report.nodeid)
    elif report.skipped:
        test_logger.warning("SKIP %s", report.nodeid)
        RUN_LOGGER.warning("SKIP %s", report.nodeid)


def pytest_sessionfinish(session: pytest.Session, exitstatus: int) -> None:
    RUN_LOGGER.info("Finished pytest session with exit status %s", exitstatus)
    RUN_LOGGER.info("Combined HTML report target: %s", REPORTS_DIR / "test_report.html")
    RUN_LOGGER.info("Per-test logs directory: %s", LOGS_DIR)
    _close_test_file_loggers()


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    selected_mode = config.getoption("--mode")

    if selected_mode is None:
        if sys.stdin is not None and sys.stdin.isatty():
            selected_mode = _prompt_test_mode()
        else:
            selected_mode = "ui"

    config.option.mode = selected_mode

    if selected_mode == "all":
        return

    skip_reason = f"Skipped in '{selected_mode}' mode"
    skip_marker = pytest.mark.skip(reason=skip_reason)

    for item in items:
        is_ui_test = item.get_closest_marker("ui") is not None
        is_api_test = item.get_closest_marker("api") is not None

        if selected_mode == "ui" and is_api_test:
            item.add_marker(skip_marker)
        if selected_mode == "api" and is_ui_test:
            item.add_marker(skip_marker)


def _get_test_file_logger(test_path: str) -> logging.Logger:
    log_key = sanitize_filename(Path(test_path).stem)
    existing_logger = TEST_FILE_LOGGERS.get(log_key)
    if existing_logger is not None:
        return existing_logger

    logger = logging.getLogger(f"testrun.{log_key}")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        log_path = LOGS_DIR / f"{log_key}.log"
        file_handler = FileHandler(log_path, mode="w", encoding="utf-8")
        file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
        logger.addHandler(file_handler)

    logger.propagate = True
    TEST_FILE_LOGGERS[log_key] = logger
    return logger


def _close_test_file_loggers() -> None:
    for logger in TEST_FILE_LOGGERS.values():
        for handler in list(logger.handlers):
            handler.close()
            logger.removeHandler(handler)
    TEST_FILE_LOGGERS.clear()


@pytest.fixture(scope="session")
def config() -> dict:
    return load_config(ROOT_DIR / "config" / "config.yaml")


@pytest.fixture(scope="session")
def base_url(config: dict) -> str:
    return get_base_url(config)


@pytest.fixture(scope="function")
def driver(config: dict):
    browser = create_driver(config)

    yield browser

    browser.quit()


@pytest.fixture(scope="function")
def login_page(driver, config: dict) -> LoginPage:
    return LoginPage(driver, timeout=config.get("timeout", 30))


@pytest.fixture(scope="function")
def dashboard_page(driver, config: dict) -> DashboardPage:
    return DashboardPage(driver, timeout=config.get("timeout", 30))


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or not report.failed:
        return

    driver_instance = item.funcargs.get("driver")
    if driver_instance is None:
        return

    screenshot_path = save_screenshot(driver_instance, SCREENSHOTS_DIR, item.nodeid)
    report.sections.append(("screenshot", str(screenshot_path)))

    if item.config.pluginmanager.hasplugin("html"):
        pytest_html = item.config.pluginmanager.getplugin("html")
        extras = getattr(report, "extras", [])
        extras.append(pytest_html.extras.image(str(screenshot_path.relative_to(REPORTS_DIR))))
        report.extras = extras
