"""Unit tests for the OrangeHRM login page object."""

from __future__ import annotations

from unittest.mock import Mock

import pytest

from pages.login_page import LoginPage


pytestmark = [pytest.mark.ui, pytest.mark.regression]


def test_open_navigates_to_login_url() -> None:
    driver = Mock()
    page = LoginPage(driver)

    page.open()

    driver.get.assert_called_once_with(LoginPage.URL)


def test_login_fills_form_then_clicks_submit() -> None:
    driver = Mock()
    page = LoginPage(driver)
    page.enter_username = Mock()
    page.enter_password = Mock()
    page.click_login = Mock()

    page.login("Admin", "admin123")

    page.enter_username.assert_called_once_with("Admin")
    page.enter_password.assert_called_once_with("admin123")
    page.click_login.assert_called_once_with()


def test_is_login_page_loaded_checks_logo_and_fields() -> None:
    driver = Mock()
    page = LoginPage(driver)
    page.is_visible = Mock(return_value=True)
    page.is_username_field_visible = Mock(return_value=True)
    page.is_password_field_visible = Mock(return_value=True)

    assert page.is_login_page_loaded() is True

    page.is_visible.assert_called_once_with(LoginPage.LOGO)


def test_login_button_state_is_exposed_by_page_object() -> None:
    driver = Mock()
    page = LoginPage(driver)
    clickable = Mock()
    clickable.is_enabled.return_value = True
    page.wait_for_clickable = Mock(return_value=clickable)

    assert page.is_login_button_enabled() is True
    page.wait_for_clickable.assert_called_once_with(LoginPage.LOGIN_BUTTON)