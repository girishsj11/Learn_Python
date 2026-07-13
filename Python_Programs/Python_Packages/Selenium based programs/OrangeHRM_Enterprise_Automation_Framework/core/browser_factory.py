"""Browser factory for Selenium WebDriver instances."""

from __future__ import annotations

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_driver(config: dict) -> webdriver.Chrome:
    options = Options()
    options.page_load_strategy = "none"
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.notifications": 2,
            "autofill.profile_enabled": False,
            "autofill.credit_card_enabled": False,
        },
    )
    if config.get("headless"):
        options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-features=PasswordLeakDetection,AutofillServerCommunication")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome(options=options)
    browser.set_page_load_timeout(config.get("timeout", 30))
    browser.maximize_window()
    return browser