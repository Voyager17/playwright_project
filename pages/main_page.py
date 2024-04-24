import os

import allure
from dotenv import load_dotenv
from playwright.sync_api import expect, Locator

from pages.base_page import BasePage
from pages.locators.locators import FindCarPageLocators as FindCarPageLoc
from pages.locators.locators import MainPageLocators as MainLoc
from pages.locators.locators import RegistrationPageLocators as RegisterLoc
from pages.locators.locators import TextColors as ColorLoc
from pages.locators.locators import Texts as TextLoc

load_dotenv()


class MainPage(BasePage):
    page_url = "/"

    @allure.step("Make the authorization")
    def login(self, login=None, password=None) -> None:
        login = login or os.getenv("LOGIN")
        password = password or os.getenv("PASSWORD")

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

    @allure.step("Check that authorization is completed by finding user'" "s id")
    def check_authorization(self, user_id=None) -> None:
        users_id = user_id or os.getenv("USERS_ID")

        self.page.hover(MainLoc.USERS_ICON_BUTTON)
        expect(self.find(MainLoc.USERS_ID_BUTTON)).to_contain_text(users_id)

    @allure.step(
        "Check the message about wrong authorization when all fields are filled"
    )
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

    @allure.step(
        "Check the message about wrong authorization when some of fields is empty"
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

    @allure.step("Check the message's color")
    def check_message_color(self, locator, expected_color) -> None:
        """
        expected_color is must be written as rgb
        example: expected_color = "rgb(234, 27, 27)"
        """
        current_color = self.find_color_of_element(locator)
        assert (
            expected_color == current_color
        ), f"Current color is different = {current_color}"

    @allure.step("Check the text in the message about wrong authorization")
    def check_error_authorization_text(self, locator) -> None:
        element: Locator = self.find(locator)
        expect(
            element, f"Locator has another text {element.text_content()}"
        ).to_contain_text(TextLoc.WRONG_CREDENTIALS_ERROR_MESSAGE)

    @allure.step(
        "Check the text in the message about wrong authorization when on of the fields is empty"
    )
    def check_error_authorization_text_empty(self, locator: str) -> None:
        element: Locator = self.find(locator)
        expect(
            element, f"Locator has another text {element.text_content()}"
        ).to_contain_text(TextLoc.EMPTY_LOGIN_ERROR_MESSAGE)

    @allure.step("Fill the car's data into the fields to find it")
    def put_data_to_find_car_by_its_number(self, number: str):
        data_field: Locator = self.find(MainLoc.CAR_NUMBER_CHECKING_FIELD)
        data_field.wait_for(state="visible")
        data_field.fill(number)

        check_car_button: Locator = self.find(MainLoc.CHECK_CAR_NUMBER_BUTTON)
        check_car_button.click()

    @allure.step("Check incorrect cases when checking car before buying")
    def check_car_before_buying_incorrect_cases(self, number: str) -> None:
        self.put_data_to_find_car_by_its_number(number)
        error_message: Locator = self.find(MainLoc.CAR_NUMBER_ERROR_TEXT)
        expect(error_message).to_contain_text(TextLoc.CAR_NUMBER_ERROR_MESSAGE)
        self.check_message_color(
            MainLoc.CAR_NUMBER_ERROR_TEXT, ColorLoc.CAR_NUMBER_ERROR_COLOR
        )

    @allure.step("Check negative cases when checking car before buying")
    def check_car_before_buying_negative_cases(
        self,
        number: str,
        expected_text: str = TextLoc.CANT_FIND_CAR_BY_NUMBER_ERROR_MESSAGE,
    ) -> None:
        """
        By default, expected_text expects error when it can't find a car by its NUMBER
        """
        self.put_data_to_find_car_by_its_number(number)
        not_found_text: Locator = self.find(FindCarPageLoc.CAR_NOT_FOUND_TEXT)
        not_found_text.wait_for(state="visible")
        self.check_matching_of_texts(
            locator=not_found_text,
            expected_text=expected_text,
            additional_info=number,
        )

    @allure.step("Check positive cases when checking car before buying")
    def check_car_before_buying_positive_cases_by_number(
        self, number: str, expected_text: str = TextLoc.GOVERNMENT_NUMBER_MESSAGE
    ) -> None:
        """
        By default, expected_text expects government number when it finds a car by its NUMBER
        """
        self.put_data_to_find_car_by_its_number(number)
        found_text: Locator = self.find(FindCarPageLoc.GOVERNMENT_NUMBER_TEXT)
        found_text.wait_for(state="visible")
        self.check_matching_of_texts(
            locator=found_text, expected_text=expected_text, additional_info=number
        )

    @allure.step("Check positive cases when checking car before buying by vin")
    def check_car_before_buying_positive_cases_by_vin(
        self, number: str, expected_text: str = TextLoc.VIN_MESSAGE
    ) -> None:
        """
        By default, expected_text expects government number when it finds a car by its NUMBER
        """
        self.put_data_to_find_car_by_its_number(number)
        found_text: Locator = self.find(FindCarPageLoc.VIN_NUMBER_TEXT).first
        found_text.wait_for(state="visible")
        self.check_matching_of_texts(
            locator=found_text, expected_text=expected_text, additional_info=number
        )
