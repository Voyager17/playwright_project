class MainPageLocators:
    REGISTRATION_BUTTON = "[data-ftid='component_header_login']"
    USERS_ICON_BUTTON = "[data-ftid='component_header_user-info-expand-controller']"
    USERS_ID_BUTTON = "[data-ftid='component_header_my-account']"
    CAR_NUMBER_ERROR_TEXT = "[data-ftid='error_message']"
    CHECK_CAR_NUMBER_BUTTON = "[data-ftid='autostory-widget_submit-button']"
    CAR_NUMBER_CHECKING_FIELD = "[data-ftid='autostory-widget_input']"


class Texts:
    CAR_NUMBER_ERROR = "Введите корректный VIN / № кузова / госномер"
    EMPTY_LOGIN_ERROR = "Поле должно быть заполнено"
    WRONG_CREDENTIALS_ERROR = "Данные для входа неверны"


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
