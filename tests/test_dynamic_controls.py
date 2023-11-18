from telnetlib import EC

import pytest
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import DynamicControlLocators


@pytest.fixture(scope="function")
def web_page():
    web_page = WebPage("Chrome")
    web_page.open_page(DynamicControlLocators.main_url)
    yield web_page
    web_page.driver.quit()


def test_dynamic_controls_page(web_page):
    response = requests.get(DynamicControlLocators.main_url)
    assert response.status_code == 200


def test_enable_disable(web_page):
    button = web_page.get_element(*DynamicControlLocators.enable_disable_button)
    button.click()
    wait = WebDriverWait(web_page.driver, 10)
    message = wait.until(EC.visibility_of_element_located(DynamicControlLocators.message))
    assert message.text == "It's enabled!"
    button.click()
    message = wait.until(EC.visibility_of_element_located(DynamicControlLocators.message))
    assert message.text == "It's disabled!"


def test_add_remove(web_page):
    button = web_page.get_element(*DynamicControlLocators.add_remove_button)
    checkbox = web_page.get_element(*DynamicControlLocators.checkbox)
    assert not checkbox.is_selected(), "Checkbox should be unselected"
    checkbox.click()
    assert checkbox.is_selected(), "Checkbox should be selected"
    button.click()
    wait = WebDriverWait(web_page.driver, 10)
    message = wait.until(EC.visibility_of_element_located(DynamicControlLocators.add_remove_message))
    assert message.text == "It's gone!"
    button.click()
    message = wait.until(EC.visibility_of_element_located(DynamicControlLocators.add_remove_message))
    assert message.text == "It's back!"

