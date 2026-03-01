from playwright.sync_api import sync_playwright
import pytest

def test_title():
    with sync_playwright() as p:
        # Launch browser (Chromium)
        browser = p.chromium.launch(headless=True)  # headless=False opens visible browser

        # Open new page
        page = browser.new_page()

        # Navigate to website
        page.goto("https://google.com")

        # Get and print page title
        title = page.title()
        assert "Google" in title

        # Close browser
        browser.close()