"""OrangeHRM dashboard page object."""

from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from core.base_page import BasePage


class DashboardPage(BasePage):
    """Page object for the OrangeHRM dashboard and header actions."""

    DASHBOARD_HEADER = (By.XPATH, "//h6[normalize-space()='Dashboard']")
    USER_MENU = (By.CSS_SELECTOR, ".oxd-userdropdown-tab")
    LOGOUT_BUTTON = (By.XPATH, "//a[normalize-space()='Logout']")
    SIDEBAR = (By.CSS_SELECTOR, ".oxd-sidepanel")

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        super().__init__(driver, timeout)

    def is_dashboard_loaded(self) -> bool:
        return self.is_visible(self.DASHBOARD_HEADER)

    def get_page_header(self) -> str:
        return self.get_text(self.DASHBOARD_HEADER)

    def get_profile_menu_text(self) -> str:
        return self.get_text(self.USER_MENU)

    def open_profile_menu(self) -> None:
        self.click(self.USER_MENU)

    def logout(self) -> None:
        self.open_profile_menu()
        self.click(self.LOGOUT_BUTTON)

    def is_sidebar_visible(self) -> bool:
        return self.is_visible(self.SIDEBAR)
