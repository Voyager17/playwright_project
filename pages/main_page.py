from CREDENTIALS import PASSWORD, LOGIN, USERS_ID
from pages.base_page import BasePage
from pages.locators.locators import MainPageLocators as MainLoc
from pages.locators.locators import RegistrationPageLocators as RegisterLoc
from pages.locators.locators import TextColors as ColorLoc
from pages.locators.locators import Texts as TextLoc
from playwright.sync_api import expect, Locator


class MainPage(BasePage):
    page_url = "/"

    def login(self, login=LOGIN, password=PASSWORD) -> None:
        registration_button: Locator = self.find(MainLoc.REGISTRATION_BUTTON)
        login_field: Locator = self.find(RegisterLoc.LOGIN_BUTTON)
        password_field: Locator = self.find(RegisterLoc.PASSWORD_BUTTON)
        submit_button: Locator = self.find(RegisterLoc.SIGN_BUTTON)

        self.open()
        self.page.wait_for_load_state("domcontentloaded")

        registration_button.wait_for(state="visible")
        registration_button.click()
        self.page.wait_for_load_state("domcontentloaded")

        login_field.wait_for(state="visible")
        login_field.fill(login)

        password_field.wait_for(state="visible")
        password_field.fill(password)

        submit_button.wait_for(state="visible")
        submit_button.click()
        self.page.wait_for_load_state("domcontentloaded")

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
        ).to_contain_text(TextLoc.WRONG_CREDENTIALS_ERROR)

    def check_error_authorization_text_empty(self, locator) -> None:
        element: Locator = self.find(locator)
        expect(
            element, f"Locator has another text {element.text_content()}"
        ).to_contain_text(TextLoc.EMPTY_LOGIN_ERROR)

    def check_car_before_buying_incorrect_cases(self, number) -> None:
        data_field: Locator = self.find(MainLoc.CAR_NUMBER_CHECKING_FIELD)
        data_field.wait_for(state="visible")
        data_field.fill(number)

        check_car_button: Locator = self.find(MainLoc.CHECK_CAR_NUMBER_BUTTON)
        check_car_button.click()
        error_message: Locator = self.find(MainLoc.CAR_NUMBER_ERROR_TEXT)
        expect(error_message).to_contain_text(TextLoc.CAR_NUMBER_ERROR)
        self.check_message_color(
            MainLoc.CAR_NUMBER_ERROR_TEXT, ColorLoc.CAR_NUMBER_ERROR_COLOR
        )
