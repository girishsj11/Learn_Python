"""Dashboard verification scenarios for OrangeHRM."""

from __future__ import annotations

import pytest

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


pytestmark = [pytest.mark.ui, pytest.mark.regression]


def test_dashboard_header_and_sidebar_are_visible(driver, login_page: LoginPage, dashboard_page: DashboardPage, config: dict) -> None:
    login_page.open()
    credentials = config["credentials"]["valid"]

    login_page.login(credentials["username"], credentials["password"])

    assert dashboard_page.is_dashboard_loaded()
    assert dashboard_page.get_page_header() == "Dashboard"
    assert dashboard_page.is_sidebar_visible()


def test_profile_menu_shows_user_name_after_login(driver, login_page: LoginPage, dashboard_page: DashboardPage, config: dict) -> None:
    login_page.open()
    credentials = config["credentials"]["valid"]

    login_page.login(credentials["username"], credentials["password"])

    assert dashboard_page.is_dashboard_loaded()
    assert dashboard_page.get_profile_menu_text().strip()