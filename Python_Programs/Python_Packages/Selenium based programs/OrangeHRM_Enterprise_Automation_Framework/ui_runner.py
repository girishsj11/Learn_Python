"""Convenience runner for the UI test suite."""

from __future__ import annotations

import argparse
import sys

from main import run_sequential_suite


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run OrangeHRM UI tests")
    args, pytest_args = parser.parse_known_args(argv)
    args.pytest_args = pytest_args
    return args


def main() -> int:
    args = _parse_args(sys.argv[1:])
    return run_sequential_suite("ui", args.pytest_args)


if __name__ == "__main__":
    sys.exit(main())