"""Wait helpers for Selenium page objects."""

from __future__ import annotations

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait


def create_wait(driver: WebDriver, timeout: int = 10) -> WebDriverWait:
    return WebDriverWait(driver, timeout)