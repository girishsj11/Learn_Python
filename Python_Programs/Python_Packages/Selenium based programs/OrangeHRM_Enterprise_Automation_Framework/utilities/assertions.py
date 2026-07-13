"""Small assertion helpers for UI tests."""

from __future__ import annotations


def assert_contains_text(actual: str, expected: str) -> None:
    assert expected in actual, f"Expected '{expected}' to appear in '{actual}'"


def assert_not_empty(value: str) -> None:
    assert value.strip(), "Expected a non-empty value"