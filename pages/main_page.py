from playwright.sync_api import expect, Locator

from CREDENTIALS import PASSWORD, LOGIN, USERS_ID
from pages.base_page import BasePage
from pages.locators.locators import MainPageLocators as MainLoc
from pages.locators.locators import RegistrationPageLocators as RegisterLoc


class MainPage(BasePage):
    page_url = "/"

    def login(self, login=LOGIN, password=PASSWORD):
        self.open()
        self.find(MainLoc.REGISTRATION_BUTTON).click()
        self.find(RegisterLoc.LOGIN_BUTTON).fill(login)
        self.find(RegisterLoc.PASSWORD_BUTTON).fill(password)
        self.find(RegisterLoc.SIGN_BUTTON).click()

    def check_authorization(self):
        self.page.hover(MainLoc.USERS_ICON_BUTTON)
        expect(self.find(MainLoc.USERS_ID_BUTTON)).to_contain_text(USERS_ID)

    def check_wrong_authorization_messages_full(self):
        self.check_message_color(
            RegisterLoc.NUMBER_LOGIN_MESSAGE, RegisterLoc.ERROR_MESSAGE_COLOR
        )

        self.check_error_authorization_text(RegisterLoc.LOGIN_SIGN_ERROR)
        self.check_message_color(
            RegisterLoc.LOGIN_SIGN_ERROR, RegisterLoc.ERROR_MESSAGE_COLOR
        )

        self.check_message_color(
            RegisterLoc.PASSWORD_MESSAGE, RegisterLoc.ERROR_MESSAGE_COLOR
        )

        self.check_error_authorization_text(RegisterLoc.PASSWORD_SIGN_ERROR)
        self.check_message_color(
            RegisterLoc.PASSWORD_SIGN_ERROR, RegisterLoc.ERROR_MESSAGE_COLOR
        )

    def check_wrong_authorization_messages_empty(self):
        self.check_message_color(
            RegisterLoc.NUMBER_LOGIN_MESSAGE, RegisterLoc.ERROR_MESSAGE_COLOR
        )

        self.check_error_authorization_text_empty(RegisterLoc.LOGIN_SIGN_ERROR)
        self.check_message_color(
            RegisterLoc.LOGIN_SIGN_ERROR, RegisterLoc.ERROR_MESSAGE_COLOR
        )

        self.check_message_color(
            RegisterLoc.PASSWORD_MESSAGE, RegisterLoc.COMMON_MESSAGE_COLOR
        )

        self.check_element_is_not_visible(RegisterLoc.PASSWORD_SIGN_ERROR)

    def check_message_color(self, locator, expected_color):
        current_color = self.find_color_of_element(locator)
        assert (
            expected_color == current_color
        ), f"Current color is different = {current_color}"

    def check_error_authorization_text(self, locator):
        element: Locator = self.find(locator)
        expect(
            element, f"Locator has another text {element.text_content()}"
        ).to_contain_text("Данные для входа неверны")

    def check_error_authorization_text_empty(self, locator):
        element: Locator = self.find(locator)
        expect(
            element, f"Locator has another text {element.text_content()}"
        ).to_contain_text("Поле должно быть заполнено")
