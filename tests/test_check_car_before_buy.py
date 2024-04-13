from pages.main_page import MainPage

WRONG_NUMERALS = "12345"
WRONG_LETTERS = "ASDasd"
WRONG_MIXED = "1Aa"
WRONG_EMPTY = ""


def test_incorrect_numerals(page, authorization) -> None:
    """
    1. Open Main page after authorization
    2. Fill the number of the car with wrong numerals
    3. Check the error about it and it's color
    """
    main_page = MainPage(page)
    main_page.check_car_before_buying_incorrect_cases(WRONG_NUMERALS)


def test_incorrect_letters(page, authorization) -> None:
    """
    1. Open Main page after authorization
    2. Fill the number of the car with wrong letters
    3. Check the error about it and it's color
    """
    main_page = MainPage(page)
    main_page.check_car_before_buying_incorrect_cases(WRONG_LETTERS)


def test_incorrect_numerals_and_letters(page, authorization) -> None:
    """
    1. Open Main page after authorization
    2. Fill the number of the car with wrong numerals and letters
    3. Check the error about it and it's color
    """
    main_page = MainPage(page)
    main_page.check_car_before_buying_incorrect_cases(WRONG_MIXED)


def test_incorrect_empty_data(page, authorization) -> None:
    """
    1. Open Main page after authorization
    2. Fill the number of the car with empty data
    3. Check the error about it and it's color
    """
    main_page = MainPage(page)
    main_page.check_car_before_buying_incorrect_cases(WRONG_EMPTY)
