import pytest
import requests
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import DynamicLoadingLocators


@pytest.fixture(scope="function")
def web_page_1():
    web_page = WebPage("Chrome")
    web_page.open_page(DynamicLoadingLocators.main_url_added_not_displayed)
    yield web_page
    web_page.driver.quit()


@pytest.fixture(scope="function")
def web_page_2():
    web_page = WebPage("Chrome")
    web_page.open_page(DynamicLoadingLocators.main_url_not_added)
    yield web_page
    web_page.driver.quit()


def test_dynamic_loading_first_page(web_page_1):
    response = requests.get(DynamicLoadingLocators.main_url_added_not_displayed)
    assert response.status_code == 200


def test_dynamic_loading_second_page(web_page_2):
    response = requests.get(DynamicLoadingLocators.main_url_added_not_displayed)
    assert response.status_code == 200


def test_message_added_but_not_displayed(web_page_1):
    message = web_page_1.get_element(*DynamicLoadingLocators.hello_world_message)
    start_button = web_page_1.get_element(*DynamicLoadingLocators.start_button)
    start_button.click()
    wait = WebDriverWait(web_page_1.driver, 10)
    wait.until(EC.visibility_of_element_located(DynamicLoadingLocators.loading))
    wait.until(EC.invisibility_of_element_located(DynamicLoadingLocators.loading))
    assert message.is_displayed()


def test_message_added_after_loading(web_page_2):
    assert not web_page_2.check_if_exists(DynamicLoadingLocators.hello_world_message)
    start_button = web_page_2.get_element(*DynamicLoadingLocators.start_button)
    start_button.click()
    wait = WebDriverWait(web_page_2.driver, 10)
    wait.until(EC.visibility_of_element_located(DynamicLoadingLocators.loading))
    wait.until(EC.invisibility_of_element_located(DynamicLoadingLocators.loading))
    assert web_page_2.get_element(*DynamicLoadingLocators.hello_world_message)
    assert web_page_2.get_element(*DynamicLoadingLocators.hello_world_message).is_displayed()

