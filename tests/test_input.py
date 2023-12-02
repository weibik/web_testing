import random
import time

import pytest
import requests
from selenium.webdriver import Keys

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import InputLocators


@pytest.fixture(scope="function")
def web_page(request):
    web_page = WebPage("Chrome")
    web_page.open_page(InputLocators.main_url)
    yield web_page
    web_page.driver.quit()


def test_input_page(web_page):
    response = requests.get(InputLocators.main_url)
    assert response.status_code == 200


def test_input(web_page):
    input_field = web_page.get_element(*InputLocators.input_field)
    default_num = random.randrange(100)
    input_field.send_keys(default_num)
    assert input_field.get_attribute("value") == str(default_num)
    increase_num = random.randrange(100)
    decrease_num = random.randrange(100)
    for i in range(increase_num):
        input_field.send_keys(Keys.UP)
    for i in range(decrease_num):
        input_field.send_keys(Keys.DOWN)
    assert input_field.get_attribute("value") == str(default_num + increase_num - decrease_num)
