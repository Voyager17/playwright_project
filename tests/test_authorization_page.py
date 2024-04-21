import allure
import pytest
from pages.main_page import MainPage

WRONG_PASSWORD: str = "wrong_password43734737"
WRONG_LOGIN: str = "wrong_login7347347"
EMPTY_LOGIN: str = ""
EMPTY_PASSWORD: str = ""


@pytest.mark.regression
@pytest.mark.bug
@allure.feature("Authorization")
@allure.story("User tries to login")
@allure.title("Check logging in with right data")
def test_authorization(page, authorization) -> None:
    """
    1. Open Main page
    2. Make the authorization with right Credentials
    3. Check user's id via user's icon
    """
    main_page = MainPage(page)
    main_page.open()
    main_page.check_authorization()


@pytest.mark.regression
@pytest.mark.bug
@allure.feature("Authorization")
@allure.story("User tries to login with wrong data")
@allure.title("Check logging in with wrong login")
def test_log_with_wrong_login(page) -> None:
    """
    1. Open Main page
    2. Make the authorization with wrong login
    3. Check all errors messages and their colors
    """
    main_page = MainPage(page)
    main_page.open()
    main_page.login(login=WRONG_LOGIN)
    main_page.check_wrong_authorization_messages_full()


@pytest.mark.regression
@pytest.mark.bug
@allure.feature("Authorization")
@allure.story("User tries to login with wrong data")
@allure.title("Check logging in with wrong password")
def test_log_with_wrong_password(page) -> None:
    """
    1. Open Main page
    2. Make the authorization with wrong password
    3. Check all errors messages and their colors
    """
    main_page = MainPage(page)
    main_page.open()
    main_page.login(password=WRONG_PASSWORD)
    main_page.check_wrong_authorization_messages_full()


@pytest.mark.regression
@pytest.mark.bug
@allure.feature("Authorization")
@allure.story("User tries to login with wrong data")
@allure.title("Check logging in with wrong login and password")
def test_log_with_wrong_all(page) -> None:
    """
    1. Open Main page
    2. Make the authorization with wrong login and password
    3. Check all errors messages and their colors
    """
    main_page = MainPage(page)
    main_page.open()
    main_page.login(login=WRONG_PASSWORD, password=WRONG_PASSWORD)
    main_page.check_wrong_authorization_messages_full()


@pytest.mark.regression
@pytest.mark.bug
@allure.feature("Authorization")
@allure.story("User tries to login with wrong data")
@allure.title("Check logging in with empty login")
def test_log_with_empty_login(page) -> None:
    """
    1. Open Main page
    2. Make the authorization with empty login
    3. Check all errors messages and their colors
    """
    main_page = MainPage(page)
    main_page.open()
    main_page.login(login=EMPTY_LOGIN)
    main_page.check_wrong_authorization_messages_empty()


@pytest.mark.regression
@pytest.mark.bug
@allure.feature("Authorization")
@allure.story("User tries to login with wrong data")
@allure.title("Check logging in with empty password")
def test_log_with_empty_password(page) -> None:
    """
    1. Open Main page
    2. Make the authorization with empty password
    3. Check all errors messages and their colors
    """
    main_page = MainPage(page)
    main_page.open()
    main_page.login(password=EMPTY_PASSWORD)
    main_page.check_wrong_authorization_messages_full()


@pytest.mark.regression
@pytest.mark.bug
@allure.feature("Authorization")
@allure.story("User tries to login with wrong data")
@allure.title("Check logging in with empty login and password")
def test_log_with_empty_all(page) -> None:
    """
    1. Open Main page
    2. Make the authorization with empty login and password
    3. Check all errors messages and their colors
    """
    main_page = MainPage(page)
    main_page.open()
    main_page.login(login=EMPTY_LOGIN, password=EMPTY_PASSWORD)
    main_page.check_wrong_authorization_messages_empty()
