import pytest
import requests

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import FormAuthLocators


@pytest.fixture(scope="function")
def web_page():
    web_page = WebPage("Chrome")
    web_page.open_page(FormAuthLocators.main_url)
    yield web_page
    web_page.driver.quit()


def test_form_auth_first_page(web_page):
    response = requests.get(FormAuthLocators.main_url)
    assert response.status_code == 200


def test_correct_login(web_page):
    username = web_page.get_element(*FormAuthLocators.user_name_field)
    password = web_page.get_element(*FormAuthLocators.password_field)
    username.send_keys(FormAuthLocators.valid_nickname)
    password.send_keys(FormAuthLocators.valid_password)
    web_page.get_element(*FormAuthLocators.loggin_button).click()
    web_page.wait_for_visibility(*FormAuthLocators.secure_area_message, 5)


def test_incorrect_login(web_page):
    username = web_page.get_element(*FormAuthLocators.user_name_field)
    password = web_page.get_element(*FormAuthLocators.password_field)
    username.send_keys(FormAuthLocators.invalid_nickname)
    password.send_keys(FormAuthLocators.invalid_password)
    web_page.get_element(*FormAuthLocators.loggin_button).click()
    web_page.wait_for_visibility(*FormAuthLocators.invalid_auth_warning, 5)
    assert not web_page.check_if_visible(*FormAuthLocators.secure_area_message)


def test_security(web_page):
    assert "https://" in web_page.driver.current_url
    # What can be added in more detailed authentication page?
    # 1 - Remember me
    # 2 - Different screen seizes
    # 3 - Logout after some time
    # 4 - Logout after unsuccessful attempts
