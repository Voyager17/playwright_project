from playwright.sync_api import expect

from CREDENTIALS import PASSWORD, LOGIN, USERS_ID
from pages.base_page import BasePage
from pages.locators.locators import MainPageLocators as LC
from pages.locators.locators import RegistrationPageLocators as LOC


class MainPage(BasePage):
    page_url = "/"

    def login(self):
        self.open()
        self.find(LC.REGISTRATION_BUTTON).click()
        self.find(LOC.LOGIN_BUTTON).fill(LOGIN)
        self.find(LOC.PASSWORD_BUTTON).fill(PASSWORD)
        self.find(LOC.SIGN_BUTTON).click()

    def check_authorization(self):
        self.page.hover(LC.USERS_ICON_BUTTON)
        expect(self.find(LC.USERS_ID_BUTTON)).to_contain_text(USERS_ID)
