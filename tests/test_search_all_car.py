import allure
import pytest
from pages.car_page import CarPage

BMW = "BMW"
AUDI = "Audi"
ROLLS_ROYCE = "Rolls-Royce"
ALFA_ROMEO = "Alfa Romeo"
LYNK_AND_CO = "Lynk & Co"

LADA = "Лада"
LUAZ = "ЛуАЗ"
ZIL = "ЗИЛ"
OTHER_CARS = "Прочие авто"

TYPE_OF_THE_CAR = "all"


@pytest.mark.regression
@pytest.mark.smoke
@allure.feature("Search cars")
@allure.story("User searches all cars with english mark")
@allure.title("Search for a car whose mark consists of a single english word")
def test_search_a_car_one_english_name(page):
    """
    1. Open the page with searching of all cars
    2. Fill a mark field
    3. Press the button search
    4. Check the url after searching
    """
    car_page = CarPage(page)
    car_page.open()
    car_page.search_a_car(mark=AUDI, type_of_the_car=TYPE_OF_THE_CAR)
    car_page.check_a_result_after_searching(
        mark=AUDI, is_russian_mark=False, type_of_the_car=TYPE_OF_THE_CAR
    )


@pytest.mark.regression
@allure.feature("Search cars")
@allure.story("User searches all cars with english mark")
@allure.title("Search for a car whose mark consists of two english words")
def test_search_a_car_two_english_name(page):
    """
    1. Open the page with searching of all cars
    2. Fill a mark field
    3. Press the button search
    4. Check the url after searching
    """
    car_page = CarPage(page)
    car_page.open()
    car_page.search_a_car(mark=ALFA_ROMEO, type_of_the_car=TYPE_OF_THE_CAR)
    car_page.check_a_result_after_searching(
        mark=ALFA_ROMEO, is_russian_mark=False, type_of_the_car=TYPE_OF_THE_CAR
    )


@pytest.mark.regression
@allure.feature("Search cars")
@allure.story("User searches all cars with english mark")
@allure.title(
    "Search for a car whose mark consists of a single english word with capital letters"
)
def test_search_a_car_capslock_english_name(page):
    """
    1. Open the page with searching of all cars
    2. Fill a mark field
    3. Press the button search
    4. Check the url after searching
    """
    car_page = CarPage(page)
    car_page.open()
    car_page.search_a_car(mark=BMW, type_of_the_car=TYPE_OF_THE_CAR)
    car_page.check_a_result_after_searching(
        mark=BMW, is_russian_mark=False, type_of_the_car=TYPE_OF_THE_CAR
    )


@pytest.mark.regression
@allure.feature("Search cars")
@allure.story("User searches all cars with english mark")
@allure.title("Search for a car whose mark consists of two english words with a hyphen")
def test_search_a_car_hyphened_english_name(page):
    """
    1. Open the page with searching of all cars
    2. Fill a mark field
    3. Press the button search
    4. Check the url after searching
    """
    car_page = CarPage(page)
    car_page.open()
    car_page.search_a_car(mark=ROLLS_ROYCE, type_of_the_car=TYPE_OF_THE_CAR)
    car_page.check_a_result_after_searching(
        mark=ROLLS_ROYCE, is_russian_mark=False, type_of_the_car=TYPE_OF_THE_CAR
    )


@pytest.mark.regression
@allure.feature("Search cars")
@allure.story("User searches all cars with english mark")
@allure.title(
    "Search for a car whose mark consists of two english words with a ampersand"
)
def test_search_a_car_ampersand_english_name(page):
    """
    1. Open the page with searching of all cars
    2. Fill a mark field
    3. Press the button search
    4. Check the url after searching
    """
    car_page = CarPage(page)
    car_page.open()
    car_page.search_a_car(mark=LYNK_AND_CO, type_of_the_car=TYPE_OF_THE_CAR)
    car_page.check_a_result_after_searching(
        mark=LYNK_AND_CO, is_russian_mark=False, type_of_the_car=TYPE_OF_THE_CAR
    )


@pytest.mark.regression
@pytest.mark.smoke
@allure.feature("Search cars")
@allure.story("User searches all cars with russian mark")
@allure.title("Search for a car whose mark consists of a single russian word")
def test_search_a_car_one_russian_name(page):
    """
    1. Open the page with searching of all cars
    2. Fill a mark field
    3. Press the button search
    4. Check the url after searching
    """
    car_page = CarPage(page)
    car_page.open()
    car_page.search_a_car(mark=LADA, type_of_the_car=TYPE_OF_THE_CAR)
    car_page.check_a_result_after_searching(
        mark=LADA, is_russian_mark=True, type_of_the_car=TYPE_OF_THE_CAR
    )


@pytest.mark.regression
@allure.feature("Search cars")
@allure.story("User searches all cars with russian mark")
@allure.title(
    "Search for a car whose mark consists of a single russian word with capital and common letters"
)
def test_search_a_car_mixed_capslock_russian_name(page):
    """
    1. Open the page with searching of all cars
    2. Fill a mark field
    3. Press the button search
    4. Check the url after searching
    """
    car_page = CarPage(page)
    car_page.open()
    car_page.search_a_car(mark=LUAZ, type_of_the_car=TYPE_OF_THE_CAR)
    car_page.check_a_result_after_searching(
        mark=LUAZ, is_russian_mark=True, type_of_the_car=TYPE_OF_THE_CAR
    )


@pytest.mark.regression
@allure.feature("Search cars")
@allure.story("User searches all cars with russian mark")
@allure.title(
    "Search for a car whose mark consists of a single russian word with capital letters"
)
def test_search_a_car_capslock_russian_name(page):
    """
    1. Open the page with searching of all cars
    2. Fill a mark field
    3. Press the button search
    4. Check the url after searching
    """
    car_page = CarPage(page)
    car_page.open()
    car_page.search_a_car(mark=ZIL, type_of_the_car=TYPE_OF_THE_CAR)
    car_page.check_a_result_after_searching(
        mark=ZIL, is_russian_mark=True, type_of_the_car=TYPE_OF_THE_CAR
    )


@pytest.mark.regression
@allure.feature("Search cars")
@allure.story("User searches all cars with russian mark")
@allure.title("Search for a car whose mark consists of two russian words")
def test_search_a_car_two_russian_name(page):
    """
    1. Open the page with searching of all cars
    2. Fill a mark field
    3. Press the button search
    4. Check the url after searching
    """
    car_page = CarPage(page)
    car_page.open()
    car_page.search_a_car(mark=OTHER_CARS, type_of_the_car=TYPE_OF_THE_CAR)
    car_page.check_a_result_after_searching(
        mark=OTHER_CARS, is_russian_mark=True, type_of_the_car=TYPE_OF_THE_CAR
    )
