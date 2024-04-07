from pages.main_page import MainPage

WRONG_PASSWORD = "wrong_password43734737"
WRONG_LOGIN = "wrong_login7347347"
EMPTY_LOGIN = ""
EMPTY_PASSWORD = ""


def test_authorization(page, authorization):
    """
    1. Open Main page
    2. Make the authorization with right Credentials
    3. Check user's id via user's icon
    """
    main_page = MainPage(page)
    main_page.open()
    main_page.check_authorization()


def test_log_with_wrong_login(page):
    """
    1. Open Main page
    2. Make the authorization with wrong login
    3. Check all errors messages and their colors
    """
    main_page = MainPage(page)
    main_page.open()
    main_page.login(login=WRONG_LOGIN)
    main_page.check_wrong_authorization_messages_full()


def test_log_with_wrong_password(page):
    """
    1. Open Main page
    2. Make the authorization with wrong password
    3. Check all errors messages and their colors
    """
    main_page = MainPage(page)
    main_page.open()
    main_page.login(password=WRONG_PASSWORD)
    main_page.check_wrong_authorization_messages_full()


def test_log_with_wrong_all(page):
    """
    1. Open Main page
    2. Make the authorization with wrong login and password
    3. Check all errors messages and their colors
    """
    main_page = MainPage(page)
    main_page.open()
    main_page.login(login=WRONG_PASSWORD, password=WRONG_PASSWORD)
    main_page.check_wrong_authorization_messages_full()


def test_log_with_empty_login(page):
    """
    1. Open Main page
    2. Make the authorization with empty login
    3. Check all errors messages and their colors
    """
    main_page = MainPage(page)
    main_page.open()
    main_page.login(login=EMPTY_LOGIN)
    main_page.check_wrong_authorization_messages_empty()


def test_log_with_empty_password(page):
    """
    1. Open Main page
    2. Make the authorization with empty password
    3. Check all errors messages and their colors
    """
    main_page = MainPage(page)
    main_page.open()
    main_page.login(password=EMPTY_PASSWORD)
    main_page.check_wrong_authorization_messages_full()


def test_log_with_empty_all(page):
    """
    1. Open Main page
    2. Make the authorization with empty login and password
    3. Check all errors messages and their colors
    """
    main_page = MainPage(page)
    main_page.open()
    main_page.login(login=EMPTY_LOGIN, password=EMPTY_PASSWORD)
    main_page.check_wrong_authorization_messages_empty()
