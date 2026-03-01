import re
from playwright.sync_api import expect,Page

def test_google_search_engine(page:Page):
    page.wait_for_timeout(3000)
    page.goto("https://www.google.com/")

    try:
        page.get_by_role('button',name='Accept all').click(timeout=2000)
    except Exception as e:
        print(f"No Popups - {e}")

    page.get_by_role("combobox",name="search").fill("Playwright Automation")
    page.keyboard.press("Enter")

    expect(page).to_have_title(re.compile("Automation", re.IGNORECASE))


def test_has_title(page:Page):
    page.goto("https://www.google.com/")
    # Expect a title "to contain" a substring.
    expect(page).to_have_url("https://www.google.com/")
    expect(page).to_have_title(re.compile("Google"))

def test_get_started_link(page:Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()