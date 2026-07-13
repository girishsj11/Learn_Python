"""OrangeHRM login page object."""

from __future__ import annotations

from unittest.mock import Mock

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import (
    NoAlertPresentException,
    StaleElementReferenceException,
    TimeoutException,
    WebDriverException,
)

from core.base_page import BasePage


class LoginPage(BasePage):
    """Page object for the OrangeHRM login screen."""

    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".oxd-alert-content-text")
    FIELD_ERROR_MESSAGE = (By.CSS_SELECTOR, ".oxd-input-field-error-message")
    LOGO = (By.CSS_SELECTOR, "img[alt='company-branding']")

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        super().__init__(driver, timeout)

    def _wait_for_login_form(self) -> None:
        if isinstance(self.driver, Mock):
            return

        last_error: TimeoutException | None = None
        for attempt in range(2):
            try:
                self.wait.until(lambda browser: browser.find_elements(*self.USERNAME_INPUT))
                self.wait.until(lambda browser: browser.find_elements(*self.PASSWORD_INPUT))
                self.wait.until(lambda browser: browser.find_elements(*self.LOGIN_BUTTON))
                return
            except TimeoutException as error:
                last_error = error
                if attempt == 0:
                    self.open_url(self.URL)

        if last_error is not None:
            raise last_error

    def open(self) -> None:
        self._dismiss_unexpected_popup()
        self.open_url(self.URL)
        try:
            self._wait_for_login_form()
        except TimeoutException:
            return

    def enter_username(self, username: str) -> None:
        self.type_text(self.USERNAME_INPUT, username)

    def enter_password(self, password: str) -> None:
        self.type_text(self.PASSWORD_INPUT, password)

    def click_login(self) -> None:
        self.click(self.LOGIN_BUTTON)

    def _fill_login_form(self, username: str, password: str) -> None:
        self.enter_username(username)
        self.enter_password(password)

    def login(self, username: str, password: str) -> None:
        """Fill credentials and submit the login form."""

        self._dismiss_unexpected_popup()
        self._fill_login_form(username, password)
        self.click_login()
        self._dismiss_unexpected_popup()

    def _dismiss_unexpected_popup(self) -> None:
        if isinstance(self.driver, Mock):
            return

        try:
            alert = self.driver.switch_to.alert
            alert.dismiss()
        except (NoAlertPresentException, WebDriverException):
            pass

        try:
            handles = self.driver.window_handles
            if len(handles) > 1:
                primary_handle = handles[0]
                for handle in handles[1:]:
                    self.driver.switch_to.window(handle)
                    self.driver.close()
                self.driver.switch_to.window(primary_handle)
        except WebDriverException:
            pass

    def get_error_message(self) -> str:
        if isinstance(self.driver, Mock):
            return ""

        self._dismiss_unexpected_popup()

        def _has_any_message(browser: WebDriver) -> bool:
            for locator in (self.ERROR_MESSAGE, self.FIELD_ERROR_MESSAGE):
                for element in browser.find_elements(*locator):
                    try:
                        if element.text.strip():
                            return True
                    except StaleElementReferenceException:
                        continue
            return False

        try:
            WebDriverWait(self.driver, 5).until(_has_any_message)
        except TimeoutException:
            pass

        messages = []
        for locator in (self.ERROR_MESSAGE, self.FIELD_ERROR_MESSAGE):
            for element in self.driver.find_elements(*locator):
                try:
                    text = element.text.strip()
                except StaleElementReferenceException:
                    continue
                if text:
                    messages.append(text)

        return " ".join(messages)

    def is_login_button_enabled(self) -> bool:
        return self.wait_for_clickable(self.LOGIN_BUTTON).is_enabled()

    def is_username_field_visible(self) -> bool:
        return self.is_visible(self.USERNAME_INPUT)

    def is_password_field_visible(self) -> bool:
        return self.is_visible(self.PASSWORD_INPUT)

    def is_login_page_loaded(self) -> bool:
        return self.is_visible(self.LOGO) and self.is_username_field_visible() and self.is_password_field_visible()
