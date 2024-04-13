import pytest
from pages.main_page import MainPage
from playwright.sync_api import BrowserContext, Page


@pytest.fixture()
def page(playwright, context: BrowserContext) -> Page:
    playwright.selectors.set_test_id_attribute("id")
    page: Page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    return page


@pytest.fixture()
def authorization(page) -> None:
    authorization_page = MainPage(page)
    authorization_page.login()
