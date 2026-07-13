"""General helpers used across the framework."""

from __future__ import annotations

import re


def sanitize_filename(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("._-")
    return cleaned or "artifact"


def normalize_whitespace(value: str) -> str:
    return " ".join(value.split())