"""Positive login scenarios for OrangeHRM."""

from __future__ import annotations

import pytest

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


pytestmark = [pytest.mark.ui, pytest.mark.positive, pytest.mark.regression]


@pytest.mark.smoke
def test_valid_login_shows_dashboard(driver, login_page: LoginPage, dashboard_page: DashboardPage, config: dict) -> None:
    login_page.open()
    assert login_page.is_login_page_loaded()

    credentials = config["credentials"]["valid"]
    login_page.login(credentials["username"], credentials["password"])

    assert dashboard_page.is_dashboard_loaded()
    assert dashboard_page.get_page_header() == "Dashboard"
    assert dashboard_page.is_sidebar_visible()


def test_logout_returns_to_login_page(driver, login_page: LoginPage, dashboard_page: DashboardPage, config: dict) -> None:
    login_page.open()
    credentials = config["credentials"]["valid"]
    login_page.login(credentials["username"], credentials["password"])

    assert dashboard_page.is_dashboard_loaded()
    dashboard_page.logout()

    assert login_page.is_login_page_loaded()


def test_login_page_fields_are_visible_before_submit(login_page: LoginPage) -> None:
    login_page.open()

    assert login_page.is_login_page_loaded()
    assert login_page.is_username_field_visible()
    assert login_page.is_password_field_visible()
    assert login_page.is_login_button_enabled()
