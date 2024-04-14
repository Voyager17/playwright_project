import allure
from playwright.sync_api import Page, Locator, expect


class BasePage:
    base_url = "https://www.drom.ru"
    page_url = None

    def __init__(self, page: Page) -> None:
        self.page = page

    @allure.step("Open the page")
    def open(self) -> None:
        if self.page_url:
            self.page.goto(f"{self.base_url}{self.page_url}")
        else:
            raise NotImplementedError("Page can not be opened by URL for this page")

    @allure.step("Find element by locator")
    def find(self, locator: str) -> Locator:
        return self.page.locator(locator)

    @allure.step("Find a color of the element")
    def find_color_of_element(self, locator: str) -> str:
        element: Locator = self.find(locator)
        color_value: str = element.evaluate("el => getComputedStyle(el).color")
        return color_value

    @allure.step("Check a color of the message")
    def check_message_color(self, locator: str, expected_color) -> None:
        """
        Expected_color must be written as a str of rgb format
        Example: expected_color = "rgb(74, 74, 74)"
        """
        current_color: str = self.find_color_of_element(locator)
        assert (
            expected_color == current_color
        ), f"Current color is different = {current_color}"

    @allure.step("Check that element isn't visible")
    def check_element_is_not_visible(self, locator: str) -> None:
        element: Locator = self.find(locator)
        expect(element, f"Element {element} is visible").not_to_be_visible()

    @staticmethod
    @allure.step("Check that text of the element is matching")
    def check_matching_of_texts(
        locator: Locator, expected_text: str, additional_info: str = ""
    ) -> None:
        """
        Locator of the text that you are looking for
        Expected_text is the text that you are expecting
        Additional_info could be anything for example the number/vin of the car
        """
        expect(
            locator,
            f"Text is different: {locator.text_content()}",
        ).to_contain_text(expected_text + f"{additional_info}")
