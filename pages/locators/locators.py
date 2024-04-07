class MainPageLocators:
    REGISTRATION_BUTTON = "[data-ftid='component_header_login']"
    USERS_ICON_BUTTON = "[data-ftid='component_header_user-info-expand-controller']"
    USERS_ID_BUTTON = "[data-ftid='component_header_my-account']"


class RegistrationPageLocators:
    LOGIN_BUTTON = "[id='sign']"
    PASSWORD_BUTTON = "#password"
    SIGN_BUTTON = "#signbutton"
    NUMBER_LOGIN_MESSAGE = ["for='sign'"]
    LOGIN_SIGN_ERROR = "#sign_errors"
    PASSWORD_MESSAGE = ["for='password'"]
    PASSWORD_SIGN_ERROR = "#password_errors"
    ERROR_MESSAGE_COLOR = "#ea1b1b"


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
