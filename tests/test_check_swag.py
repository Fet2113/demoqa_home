from pages.swag_labs import SwagLabs


def test_icon_exist(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    swag_labs_page.click_on_the_icon()
    assert swag_labs_page.exist_icon()

def test_user_name_exist(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    assert swag_labs_page.input()

def test_password_exist(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    assert swag_labs_page.input()
# Опять не идет селениум(((