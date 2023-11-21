import os
from glob import glob
from time import sleep

import pytest
import requests

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import FloatingMenuLocators


@pytest.fixture(scope="function")
def web_page(request):
    web_page = WebPage("Chrome")
    web_page.open_page(FloatingMenuLocators.main_url)
    yield web_page
    web_page.driver.quit()


def test_floating_menu_first_page(web_page):
    response = requests.get(FloatingMenuLocators.main_url)
    assert response.status_code == 200


def test_floating_menu(web_page):
    web_page.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    assert web_page.check_if_visible(*FloatingMenuLocators.home_button)
    assert web_page.check_if_visible(*FloatingMenuLocators.home_button)
    assert web_page.check_if_visible(*FloatingMenuLocators.news_button)
    assert web_page.check_if_visible(*FloatingMenuLocators.contact_button)
    assert web_page.check_if_visible(*FloatingMenuLocators.about_button)
