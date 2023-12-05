import pytest
import requests
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import LargeDOMLocators


@pytest.fixture(scope="function")
def web_page():
    web_page = WebPage("Chrome")
    web_page.open_page(LargeDOMLocators.main_url)
    yield web_page
    web_page.driver.quit()


def test_large_dom_page(web_page):
    response = requests.get(LargeDOMLocators.main_url)
    assert response.status_code == 200


def test_large_dom(web_page):
    assert web_page.check_if_exists(*LargeDOMLocators.table)
    table_body = web_page.driver.find_element(By.TAG_NAME, "tbody")
    rows = table_body.find_elements(By.TAG_NAME, "tr")
    number_of_rows = 50
    assert len(rows) == number_of_rows
