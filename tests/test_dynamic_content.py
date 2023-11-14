import pytest
import requests

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import DynamicContentLocators


@pytest.fixture(scope="function")
def web_page():
    web_page = WebPage("Chrome")
    web_page.open_page(DynamicContentLocators.main_url)
    yield web_page
    web_page.driver.quit()


def test_dynamic_page(web_page):
    response = requests.get(DynamicContentLocators.main_url)
    assert response.status_code == 200


def test_static_page(web_page):
    response = requests.get(DynamicContentLocators.main_url_static)
    assert response.status_code == 200
