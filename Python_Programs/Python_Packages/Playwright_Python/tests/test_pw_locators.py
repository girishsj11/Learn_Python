from playwright.sync_api import Page,expect
import re

def test_builtin_locators(page:Page):
    url = "https://testautomationpractice.blogspot.com/p/playwrightpractice.html"
    page.goto(url)
    page.wait_for_timeout(3000)

    # get_by_alt_text
    expect(page.get_by_alt_text("logo image")).to_be_visible()

    #get_by_text
    expect(page.get_by_text("Playwright Logo")).to_be_visible()

    #get_by_role
    expect(page.get_by_role("button",name="start")).to_be_visible()

    #get_by_label
    expect(page.get_by_label("username")).to_be_enabled()
    page.get_by_label("username").fill("World")

    #get_by_place_holder
    expect(page.get_by_placeholder("Enter your full name")).to_be_enabled()

    assert not page.is_closed()

    #close the browser/page context
    page.close()

