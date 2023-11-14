import pytest
import requests

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import TheInternetMainPageLocators


@pytest.fixture(scope="function")
def web_page():
    web_page = WebPage("Chrome")
    web_page.open_page(TheInternetMainPageLocators.main_url)
    yield web_page
    web_page.driver.quit()
    
    
def test_main_page(web_page):
    web_page.open_page(TheInternetMainPageLocators.main_url)
    assert web_page.driver.current_url == "https://the-internet.herokuapp.com/"
    assert web_page.driver.title == "The Internet"
    response = requests.get(TheInternetMainPageLocators.main_url)
    assert response.status_code == 200


def test_ab_page_navigation(web_page):
    web_page.open_page(TheInternetMainPageLocators.main_url)
    element_ab_testing = web_page.driver.find_element(*TheInternetMainPageLocators.ab_testing_page)
    element_ab_testing.click()
    assert web_page.driver.current_url == "https://the-internet.herokuapp.com/abtest"


def test_add_remove_page_navigation(web_page):
    web_page.open_page(TheInternetMainPageLocators.main_url)
    add_remove_page_hyperlink = web_page.driver.find_element(*TheInternetMainPageLocators.add_remove_page)
    add_remove_page_hyperlink.click()
    assert web_page.driver.current_url == "https://the-internet.herokuapp.com/add_remove_elements/"
