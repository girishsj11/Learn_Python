"""API smoke coverage for OrangeHRM endpoints."""

from __future__ import annotations

import pytest
import requests


pytestmark = [pytest.mark.api, pytest.mark.smoke, pytest.mark.regression]

LOGIN_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
BASE_DOMAIN_URL = "https://opensource-demo.orangehrmlive.com"
PROTECTED_DASHBOARD_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"


def test_login_url_returns_success() -> None:
    response = requests.get(LOGIN_URL, timeout=20)

    assert response.status_code == 200


def test_login_page_contains_expected_form_elements() -> None:
    response = requests.get(LOGIN_URL, timeout=20)

    assert response.status_code == 200
    body = response.text.lower()
    assert "<auth-login" in body
    assert "login-logo-src" in body
    assert "chunk-vendors.js" in body


def test_base_domain_redirects_to_login_page() -> None:
    response = requests.get(BASE_DOMAIN_URL, timeout=20, allow_redirects=True)

    assert response.status_code == 200
    assert "/auth/login" in response.url


def test_protected_dashboard_redirects_to_login_without_session() -> None:
    response = requests.get(PROTECTED_DASHBOARD_URL, timeout=20, allow_redirects=True)

    assert response.status_code == 200
    assert "/auth/login" in response.url


def test_login_page_response_is_html() -> None:
    response = requests.get(LOGIN_URL, timeout=20)

    content_type = response.headers.get("Content-Type", "").lower()
    assert "text/html" in content_type