import pytest
import requests

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import KeyPressesLocators
from string import ascii_uppercase


@pytest.fixture(scope="function")
def web_page():
    web_page = WebPage("Chrome")
    web_page.open_page(KeyPressesLocators.main_url)
    yield web_page
    web_page.driver.quit()


def test_key_presses_page(web_page):
    response = requests.get(KeyPressesLocators.main_url)
    assert response.status_code == 200


def test_key_presses(web_page):
    input_field = web_page.get_element(*KeyPressesLocators.input_field)
    for char in ascii_uppercase:
        input_field.send_keys(char)
        assert web_page.get_element(*KeyPressesLocators.result).text == f"You entered: {char}"



