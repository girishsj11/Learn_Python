from playwright.sync_api import Playwright
import pytest

def test_pw_api(playwright:Playwright):
    request = playwright.request.new_context()
    response = request.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status == 200
    json_data = response.json()
    assert json_data["id"] == 1
    request.dispose()