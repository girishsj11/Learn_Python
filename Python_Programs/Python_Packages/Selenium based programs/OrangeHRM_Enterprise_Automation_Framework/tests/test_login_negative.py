"""Negative login scenarios for OrangeHRM."""

from __future__ import annotations

import pytest

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


pytestmark = [pytest.mark.ui, pytest.mark.negative, pytest.mark.regression]


@pytest.mark.parametrize(
    "username,password",
    [
        ("invalid_user", "admin123"),
        ("Admin", "invalid_pass"),
        ("invalid_user", "invalid_pass"),
        ("", ""),
        ("", "admin123"),
        ("Admin", ""),
    ],
)
def test_invalid_login_shows_error(
    driver,
    login_page: LoginPage,
    dashboard_page: DashboardPage,
    username: str,
    password: str,
) -> None:
    login_page.open()
    login_page.login(username, password)

    error_message = login_page.get_error_message()
    assert error_message
    assert "Invalid credentials" in error_message or "Required" in error_message
    assert login_page.is_login_page_loaded()
    assert not dashboard_page.is_dashboard_loaded()
