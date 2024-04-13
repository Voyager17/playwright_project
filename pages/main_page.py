import time as t

from CREDENTIALS import PASSWORD, LOGIN, USERS_ID
from pages.base_page import BasePage
from pages.locators.locators import MainPageLocators as MainLoc
from pages.locators.locators import RegistrationPageLocators as RegisterLoc
from pages.locators.locators import TextColors as ColorLoc
from playwright.sync_api import expect, Locator


class MainPage(BasePage):
    page_url = "/"

    def login(self, login=LOGIN, password=PASSWORD) -> None:
        self.open()
        self.find(MainLoc.REGISTRATION_BUTTON).click()
        self.find(RegisterLoc.LOGIN_BUTTON).fill(login)
        self.find(RegisterLoc.PASSWORD_BUTTON).fill(password)
        self.find(RegisterLoc.SIGN_BUTTON).click()

    def check_authorization(self) -> None:
        self.page.hover(MainLoc.USERS_ICON_BUTTON)
        expect(self.find(MainLoc.USERS_ID_BUTTON)).to_contain_text(USERS_ID)

    def check_wrong_authorization_messages_full(self) -> None:
        self.check_message_color(
            RegisterLoc.NUMBER_LOGIN_MESSAGE, ColorLoc.ERROR_MESSAGE_COLOR
        )

        self.check_error_authorization_text(RegisterLoc.LOGIN_SIGN_ERROR)
        self.check_message_color(
            RegisterLoc.LOGIN_SIGN_ERROR, ColorLoc.ERROR_MESSAGE_COLOR
        )

        self.check_message_color(
            RegisterLoc.PASSWORD_MESSAGE, ColorLoc.ERROR_MESSAGE_COLOR
        )

        self.check_error_authorization_text(RegisterLoc.PASSWORD_SIGN_ERROR)
        self.check_message_color(
            RegisterLoc.PASSWORD_SIGN_ERROR, ColorLoc.ERROR_MESSAGE_COLOR
        )

    def check_wrong_authorization_messages_empty(self) -> None:
        self.check_message_color(
            RegisterLoc.NUMBER_LOGIN_MESSAGE, ColorLoc.ERROR_MESSAGE_COLOR
        )

        self.check_error_authorization_text_empty(RegisterLoc.LOGIN_SIGN_ERROR)
        self.check_message_color(
            RegisterLoc.LOGIN_SIGN_ERROR, ColorLoc.ERROR_MESSAGE_COLOR
        )

        self.check_message_color(
            RegisterLoc.PASSWORD_MESSAGE, ColorLoc.COMMON_MESSAGE_COLOR
        )

        self.check_element_is_not_visible(RegisterLoc.PASSWORD_SIGN_ERROR)

    def check_message_color(self, locator, expected_color) -> None:
        """
        expected_color is must be written as rgb
        example: expected_color = "rgb(234, 27, 27)"
        """
        current_color = self.find_color_of_element(locator)
        assert (
            expected_color == current_color
        ), f"Current color is different = {current_color}"

    def check_error_authorization_text(self, locator) -> None:
        element: Locator = self.find(locator)
        expect(
            element, f"Locator has another text {element.text_content()}"
        ).to_contain_text("Данные для входа неверны")

    def check_error_authorization_text_empty(self, locator) -> None:
        element: Locator = self.find(locator)
        expect(
            element, f"Locator has another text {element.text_content()}"
        ).to_contain_text("Поле должно быть заполнено")

    def check_car_before_buying_incorrect_cases(self, number) -> None:
        data_field: Locator = self.find("[data-ftid='autostory-widget_input']")
        data_field.fill(number)

        check_car_button: Locator = self.find(
            "[data-ftid='autostory-widget_submit-button']"
        )
        check_car_button.click()
        t.sleep(5)

        error_message: Locator = self.find("[data-ftid='error_message']")
        expect(error_message).to_contain_text(
            "Введите корректный VIN / № кузова / госномер"
        )
        # self.check_message_color(error_message, ColorLoc.ERROR_MESSAGE_COLOR)
