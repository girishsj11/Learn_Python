"""Edge-case login scenarios for OrangeHRM."""

from __future__ import annotations

import pytest
from selenium.common.exceptions import StaleElementReferenceException

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


pytestmark = [pytest.mark.ui, pytest.mark.edge, pytest.mark.regression]


@pytest.mark.parametrize(
    "username,password,should_succeed",
    [
        (" Admin ", "admin123", False),
        ("Admin", " admin123 ", False),
        ("A" * 64, "P" * 64, False),
        ("!@#$%^&*()", "!@#$%^&*()", False),
        ("123456", "123456", False),
        ("こんにちは", "パスワード", False),
        ("   ", "   ", False),
    ],
)
def test_edge_login_inputs_show_validation(
    driver,
    login_page: LoginPage,
    dashboard_page: DashboardPage,
    username: str,
    password: str,
    should_succeed: bool,
) -> None:
    login_page.open()
    login_page.login(username, password)

    if should_succeed:
        assert dashboard_page.is_dashboard_loaded()
    else:
        assert login_page.get_error_message()
        assert not dashboard_page.is_dashboard_loaded()


def test_repeated_invalid_login_attempts_keep_user_on_login_page(
    login_page: LoginPage,
    dashboard_page: DashboardPage,
) -> None:
    login_page.open()

    for _ in range(3):
        # OrangeHRM occasionally re-renders the form after submit; retry once on stale DOM.
        error_message = ""
        for attempt in range(3):
            try:
                login_page.login("invalid_user", "invalid_pass")
                error_message = login_page.get_error_message()
                if error_message:
                    break
                login_page.open()
            except StaleElementReferenceException:
                if attempt == 2:
                    raise
                login_page.open()
        assert error_message
        assert not dashboard_page.is_dashboard_loaded()
