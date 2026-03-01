from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="Search").fill("playwright")
    page.keyboard.press("Enter")
    page.get_by_role("link", name="Playwright: Fast and reliable end-to-end testing for modern ... Playwright").click()
    page.get_by_role("link", name="Get started").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
