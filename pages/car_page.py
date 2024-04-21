import allure
from pages.base_page import BasePage
from pages.locators.locators import CarPageLocators as CarLoc


class CarPage(BasePage):
    base_url = "https://auto.drom.ru"
    page_url = "/"

    @allure.step("Search a car by its mark and type")
    def search_a_car(self, mark: str = "BMW", type_of_the_car: str = "all") -> None:
        """
        Mark is a mark of the car. As a default it's BMW
        Type_of_the_car is the conditional of the car. it could be "all", "new", "used". As a default it's all
        """
        self.pick_type_of_searching_car(type_of_the_car)
        car_mark = self.find(CarLoc.MARK_SEARCH_LINE)
        car_mark.click()
        car_mark.fill(mark)
        car_mark_advise = self.find(f'div:text("{mark.lower()} ")')
        car_mark_advise.click()
        show_button = self.find(CarLoc.SHOW_BUTTON)
        show_button.click()

    @allure.step("Check the url after searching a car")
    def check_a_result_after_searching(
        self,
        mark: str = "BMW",
        is_russian_mark: bool = False,
        type_of_the_car: str = "all",
    ) -> None:
        """
        Here we check the url after searching a car
        If the mark of the car is in Russian, use the flag is_russian_mark = True
        """
        mark = self.validate_mark(
            mark_for_validate=mark, is_russian_mark_validate=is_russian_mark
        )

        expected_url = self.create_expected_url_according_to_cars_type_and_mark(
            type_of_the_car=type_of_the_car, mark=mark
        )
        self.check_url(expected_url)

    @allure.step("Validate a car's mark")
    def validate_mark(
        self, mark_for_validate: str = "BMW", is_russian_mark_validate: bool = False
    ):
        """
        This is the function for mark validating like russian or english writing and different conditions
        """
        # Validate for russian mark
        if is_russian_mark_validate:
            mark_for_validate = self.convert_russian_mark_to_english(
                car_mark=mark_for_validate
            )

        # Need this condition for checking cases like this Lynk & Co
        # because they are written in url like lynk_and_co
        if " & " in mark_for_validate:
            mark_for_validate = mark_for_validate.replace(" & ", "_and_")

        # Need this condition for checking cases like this Alfa Romeo
        # because they are written in url like alfa_romeo
        if " " in mark_for_validate:
            mark_for_validate = mark_for_validate.replace(" ", "_")

        return mark_for_validate

    @staticmethod
    @allure.step("Convert russian mark to english")
    def convert_russian_mark_to_english(car_mark: str) -> str:
        """
        Converts a Russian car brand name to its English equivalent, if available
        """
        russian_cars: dict = {
            "лада": "Lada",
            "волга": "Volga",
            "москвич": "Moskvitch",
            "газ": "GAZ",
            "уаз": "UAZ",
            "зил": "ZIL",
            "камаз": "KamAZ",
            "маруся": "Marussia",
            "нива": "Niva",
            "луаз": "Luaz",
            "прочие авто": "Other",
        }
        mark_lower: str = car_mark.lower()

        if mark_lower in russian_cars:
            return russian_cars[mark_lower]
        else:
            return car_mark

    @allure.step("Create expected url according to car's type and mark")
    def create_expected_url_according_to_cars_type_and_mark(
        self, type_of_the_car: str = "all", mark: str = "BMW"
    ) -> str:
        """
        This function returns the url for checking according to the cars type and mark
        type_of_the_car could have 3 values: all, used, new
        mark could have different values of str
        """
        match type_of_the_car.lower():
            case "all":
                return self.base_url + f"/{mark.lower()}/all/"
            case "used":
                return self.base_url + f"/{mark.lower()}/used/all/"
            case "new":
                return self.base_url + f"/{mark.lower()}/new/all/"
            case _:
                return self.base_url + f"/{mark.lower()}/all/"

    @allure.step("Choose a type of the searching car according to its type")
    def pick_type_of_searching_car(self, type_of_the_car: str = "all") -> None:
        match type_of_the_car.lower():
            case "used":
                used_tab_button = self.find(CarLoc.USED_CAR_TAB)
                used_tab_button.click()
            case "new":
                new_tab_button = self.find(CarLoc.NEW_CAR_TAB)
                new_tab_button.click()
            case _:
                pass
