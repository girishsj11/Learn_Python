"""Configuration helpers for the OrangeHRM framework."""

from __future__ import annotations

from pathlib import Path
from typing import Any


def _parse_scalar(value: str) -> Any:
    if value in {"true", "True"}:
        return True
    if value in {"false", "False"}:
        return False
    if value.isdigit():
        return int(value)
    return value.strip('"').strip("'")


def _load_simple_yaml(text: str) -> dict[str, Any]:
    root: dict[str, Any] = {}
    stack: list[tuple[int, dict[str, Any]]] = [(0, root)]

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue

        indent = len(line) - len(line.lstrip(" "))
        key, separator, remainder = line.strip().partition(":")
        if not separator:
            continue

        while stack and indent < stack[-1][0]:
            stack.pop()

        current = stack[-1][1]
        value = remainder.strip()

        if not value:
            nested: dict[str, Any] = {}
            current[key] = nested
            stack.append((indent + 2, nested))
            continue

        current[key] = _parse_scalar(value)

    return root


def load_config(config_path: Path) -> dict[str, Any]:
    with config_path.open("r", encoding="utf-8") as config_file:
        return _load_simple_yaml(config_file.read())


def get_base_url(config: dict[str, Any]) -> str:
    base_url = config.get("base_url")
    if not base_url:
        raise ValueError("base_url is missing from config")
    return str(base_url)