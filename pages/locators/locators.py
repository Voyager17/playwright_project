class MainPageLocators:
    REGISTRATION_BUTTON = "[data-ftid='component_header_login']"
    USERS_ICON_BUTTON = "[data-ftid='component_header_user-info-expand-controller']"
    USERS_ID_BUTTON = "[data-ftid='component_header_my-account']"
    CAR_NUMBER_ERROR_TEXT = "[data-ftid='error_message']"
    CHECK_CAR_NUMBER_BUTTON = "[data-ftid='autostory-widget_submit-button']"
    CAR_NUMBER_CHECKING_FIELD = "[data-ftid='autostory-widget_input']"


class FindCarPageLocators:
    CAR_NOT_FOUND_TEXT = "[class='b-text b-text_size_default']"
    GOVERNMENT_NUMBER_TEXT = "div[data-ftid='car-info-item']:nth-child(2)"
    VIN_NUMBER_TEXT = "div[data-ftid='car-info-item']"


class Texts:
    CAR_NUMBER_ERROR_MESSAGE = "Введите корректный VIN / № кузова / госномер"
    EMPTY_LOGIN_ERROR_MESSAGE = "Поле должно быть заполнено"
    WRONG_CREDENTIALS_ERROR_MESSAGE = "Данные для входа неверны"
    CANT_FIND_CAR_BY_NUMBER_ERROR_MESSAGE = (
        "Мы не смогли найти автомобиль с указанным номером кузова "
    )
    CANT_FIND_CAR_BY_VIN_ERROR_MESSAGE = (
        "Мы не смогли найти автомобиль с указанным VIN номером "
    )
    GOVERNMENT_NUMBER_MESSAGE = "Госномер: "


class RegistrationPageLocators:
    LOGIN_BUTTON = "#sign"
    PASSWORD_BUTTON = "#password"
    SIGN_BUTTON = "#signbutton"
    NUMBER_LOGIN_MESSAGE = "[for='sign']"
    LOGIN_SIGN_ERROR = "#sign_errors"
    PASSWORD_MESSAGE = "[for='password']"
    PASSWORD_SIGN_ERROR = "#password_errors"


class TextColors:
    ERROR_MESSAGE_COLOR = "rgb(234, 27, 27)"
    COMMON_MESSAGE_COLOR = "rgb(74, 74, 74)"
    CAR_NUMBER_ERROR_COLOR = "rgb(219, 0, 26)"


class AccountCreateLocators:
    FIRST_NAME_FIELD = "firstname"
    LAST_NAME_FIELD = "lastname"
    EMAIL_FIELD = "email_address"
    PASSWORD_FILED = "password"
    CONFIRM_PASSWORD_FIELD = "password-confirmation"
    CREATE_ACCOUNT_BUTTON = "[class = 'action submit primary']"
    STRENGTH_PASSWORD = "password-strength-meter-label"
    SUCCESS_MESSAGE = "[data-ui-id='message-success']"
    CONTENT_ELEMENT = ".box-content"


class CollectionsLocators:
    NAME_OF_THE_PAGE = "[data-ui-id='page-title-wrapper']"
    NEXT_PAGE_BUTTON = "a.action.next"


class SaleLocators:
    NAME_OF_THE_PAGE = "[data-ui-id='page-title-wrapper']"
    WOMEN_DEAL_BUTTON = "[class='more button']"
