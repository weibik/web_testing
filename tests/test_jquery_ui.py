import time

import pytest
import requests
from selenium.webdriver import ActionChains

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import JQueryMenuLocators


@pytest.fixture(scope="function")
def web_page():
    web_page = WebPage("Chrome")
    web_page.open_page(JQueryMenuLocators.main_url)
    yield web_page
    web_page.driver.quit()


def test_jquery_ui_page(web_page):
    response = requests.get(JQueryMenuLocators.main_url)
    assert response.status_code == 200


def test_jquery_menu(web_page):
    enabled = web_page.get_element(*JQueryMenuLocators.enabled)
    actions = ActionChains(web_page.driver)
    actions.move_to_element(enabled).perform()
    time.sleep(1)
    downloads = web_page.get_element(*JQueryMenuLocators.downloads)
    assert web_page.driver.execute_script("return $(arguments[0]).is(':visible');", downloads)
    actions.move_to_element(downloads).perform()
    time.sleep(1)
    pdf = web_page.get_element(*JQueryMenuLocators.pdf)
    assert web_page.driver.execute_script("return $(arguments[0]).is(':visible');", pdf)

