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


def test_form_auth_first_page(web_page):
    response = requests.get(FloatingMenuLocators.main_url)
    assert response.status_code == 200

# TODO
