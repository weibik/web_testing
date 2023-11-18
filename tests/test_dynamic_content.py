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


def test_dynamic_text(web_page):
    elements = web_page.driver.find_elements(*DynamicContentLocators.row)
    elements = [element.text for element in elements]
    web_page.refresh()
    elements_after_refresh = web_page.driver.find_elements(*DynamicContentLocators.row)
    elements_after_refresh = [element.text for element in elements_after_refresh]
    for i in range(len(elements)):
        assert elements[i] != elements_after_refresh[i]


def test_static_text(web_page):
    web_page.open_page(DynamicContentLocators.main_url_static)
    elements = web_page.driver.find_elements(*DynamicContentLocators.row)
    elements = [element.text for element in elements]
    web_page.refresh()
    elements_after_refresh = web_page.driver.find_elements(*DynamicContentLocators.row)
    elements_after_refresh = [element.text for element in elements_after_refresh]
    for i in range(len(elements)):
        assert elements[i] == elements_after_refresh[i], (f"Page should be in static mode, so nothing should change "
                                                          f"after the restart, but \n{elements[i]} \n!= "
                                                          f"\n{elements_after_refresh[i]}")
