import pytest
from playwright.sync_api import (
    sync_playwright,
    Playwright,
    Browser,
    BrowserContext,
    Page,
)

from pages.main_page import MainPage


@pytest.fixture(scope="session")
def playwright() -> Playwright:
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright: Playwright) -> Browser:
    browser = playwright.chromium.launch(headless=True)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser: Browser) -> BrowserContext:
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture()
def page(context: BrowserContext) -> Page:
    page: Page = context.new_page()
    page.set_default_timeout(120000)
    page.set_viewport_size({"width": 1920, "height": 1080})
    return page


@pytest.fixture()
def authorization(page: Page) -> None:
    authorization_page = MainPage(page)
    authorization_page.login()
