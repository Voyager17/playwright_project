from pages.main_page import MainPage


def test_authorization(page, login):
    base = MainPage(page)
    base.open()
    base.check_authorization()
