"""Screenshot helpers used on test failure."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from selenium.webdriver.remote.webdriver import WebDriver

from utilities.helpers import sanitize_filename


def save_screenshot(driver: WebDriver, output_dir: Path, name: str) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{sanitize_filename(name)}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    screenshot_path = output_dir / filename
    driver.save_screenshot(str(screenshot_path))
    return screenshot_path