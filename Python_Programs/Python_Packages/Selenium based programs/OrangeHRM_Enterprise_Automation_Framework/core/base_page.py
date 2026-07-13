"""Shared browser actions for page objects."""

from __future__ import annotations

from typing import Any, List, Tuple

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.support import expected_conditions as EC

from core.wait_factory import create_wait

Locator = Tuple[str, str]


class BasePage:
    """Base class that wraps common Selenium interactions."""

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        self.driver = driver
        self.timeout = timeout
        self.wait = create_wait(driver, timeout)

    def open_url(self, url: str) -> None:
        self.driver.get(url)

    def find(self, locator: Locator) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator: Locator) -> List[WebElement]:
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator: Locator) -> None:
        last_error: StaleElementReferenceException | None = None
        for _ in range(2):
            try:
                self.wait.until(EC.element_to_be_clickable(locator)).click()
                return
            except StaleElementReferenceException as error:
                last_error = error

        if last_error is not None:
            raise last_error

    def type_text(self, locator: Locator, text: str, clear_first: bool = True) -> None:
        last_error: StaleElementReferenceException | None = None
        for _ in range(2):
            try:
                element = self.find(locator)
                if clear_first:
                    element.clear()
                element.send_keys(text)
                return
            except StaleElementReferenceException as error:
                last_error = error

        if last_error is not None:
            raise last_error

    def get_text(self, locator: Locator) -> str:
        return self.find(locator).text.strip()

    def get_attribute(self, locator: Locator, attribute_name: str) -> str | None:
        return self.find(locator).get_attribute(attribute_name)

    def is_visible(self, locator: Locator) -> bool:
        try:
            return self.find(locator).is_displayed()
        except Exception:
            return False

    def wait_for_visible(self, locator: Locator) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator: Locator) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(locator))

    def scroll_to(self, locator: Locator) -> None:
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def js_click(self, locator: Locator) -> None:
        element = self.find(locator)
        self.driver.execute_script("arguments[0].click();", element)
