import allure
from playwright.sync_api import Page, Locator


class BasePage:
    base_url = "https://www.drom.ru"
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    @allure.step("Open the page")
    def open(self):
        if self.page_url:
            self.page.goto(f"{self.base_url}{self.page_url}")
        else:
            raise NotImplementedError("Page can not be opened by URL for this page")

    @allure.step("Find element by locator")
    def find(self, locator) -> Locator:
        return self.page.locator(locator)

    @allure.step("Find a color of the element")
    def find_color_of_element(self, locator) -> str:
        element: Locator = self.find(locator)
        color_value: str = element.evaluate("el => getComputedStyle(el).color")
        return color_value

    @allure.step("Check a color of the message")
    def check_message_color(self, locator, expected_color):
        current_color: str = self.find_color_of_element(locator)
        assert (
            expected_color == current_color
        ), f"Current color is different = {current_color}"
