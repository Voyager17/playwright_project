from pages.locators.locators import Texts as TextLoc
from pages.main_page import MainPage

INCORRECT_NUMERALS_MESSAGE = "12345"
INCORRECT_LETTERS_MESSAGE = "ASDasd"
INCORRECT_MIXED_MESSAGE = "1Aa"
INCORRECT_EMPTY_MESSAGE = ""
INCORRECT_SQL_MESSAGE = "OR 1=1--"

WRONG_CAR_NUMBER_MESSAGE = "AA123AA"
WRONG_CAR_VIN_MESSAGE = "X7LLSRB1HAH548712"

POSITIVE_CAR_NUMBER = "Т589УН77"
POSITIVE_CAR_VIN = "WAUYP64B01N141245"


def test_incorrect_numerals(page) -> None:
    """
    1. Open Main page
    2. Fill the number of the car with wrong numerals
    3. Check the error about it and it's color
    """
    main_page = MainPage(page)
    main_page.open()
    main_page.check_car_before_buying_incorrect_cases(INCORRECT_NUMERALS_MESSAGE)


def test_incorrect_letters(page) -> None:
    """
    1. Open Main page
    2. Fill the number of the car with wrong letters
    3. Check the error about it and it's color
    """
    main_page = MainPage(page)
    main_page.open()
    main_page.check_car_before_buying_incorrect_cases(INCORRECT_LETTERS_MESSAGE)


def test_incorrect_numerals_and_letters(page) -> None:
    """
    1. Open Main page
    2. Fill the number of the car with wrong numerals and letters
    3. Check the error about it and it's color
    """
    main_page = MainPage(page)
    main_page.open()
    main_page.check_car_before_buying_incorrect_cases(INCORRECT_MIXED_MESSAGE)


def test_incorrect_empty_data(page) -> None:
    """
    1. Open Main page
    2. Fill the number of the car with empty data
    3. Check the error about it and it's color
    """
    main_page = MainPage(page)
    main_page.open()
    main_page.check_car_before_buying_incorrect_cases(INCORRECT_EMPTY_MESSAGE)


def test_incorrect_sql_injection(page) -> None:
    """
    1. Open Main page
    2. Fill the number of the car with SQL injection
    3. Check the error about it and it's color
    """
    main_page = MainPage(page)
    main_page.open()
    main_page.check_car_before_buying_incorrect_cases(INCORRECT_SQL_MESSAGE)


def test_wrong_car_number(page) -> None:
    """
    1. Open Main page
    2. Fill the number of the car with a wrong car's number
    3. Check the error about it
    """
    main_page = MainPage(page)
    main_page.open()
    main_page.check_car_before_buying_negative_cases(WRONG_CAR_NUMBER_MESSAGE)


def test_wrong_car_vin(page) -> None:
    """
    1. Open Main page
    2. Fill the number of the car with a wrong car's VIN
    3. Check the error about it
    """
    main_page = MainPage(page)
    main_page.open()
    main_page.check_car_before_buying_negative_cases(
        number=WRONG_CAR_VIN_MESSAGE,
        expected_text=TextLoc.CANT_FIND_CAR_BY_VIN_ERROR_MESSAGE,
    )


def test_positive_car_number(page) -> None:
    """
    1. Open Main page
    2. Fill the number of the car with a right car's number
    3. Check the number of the found car
    """
    main_page = MainPage(page)
    main_page.open()
    main_page.check_car_before_buying_positive_cases_by_number(POSITIVE_CAR_NUMBER)


def test_positive_car_vin(page) -> None:
    """
    1. Open Main page
    2. Fill the number of the car with a right car's VIN
    3. Check the vin of the found car
    """
    main_page = MainPage(page)
    main_page.open()
    main_page.check_car_before_buying_positive_cases_by_vin(POSITIVE_CAR_VIN)
