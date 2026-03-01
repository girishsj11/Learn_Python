import pytest
from playwright.async_api import async_playwright


@pytest.mark.asyncio
async def test_google_title():
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=False)

        # Create new page
        page = await browser.new_page()

        # Navigate to Google
        await page.goto("https://www.google.com")

        # Get page title
        title = await page.title()

        # Expected title comparison
        expected_title = "Google"
        assert title == expected_title, f"Expected '{expected_title}', but got '{title}'"

        await browser.close()