import pytest
import requests
from selenium.webdriver.common.by import By

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import ShadoDOMLocators


@pytest.fixture(scope="function")
def web_page():
    web_page = WebPage("Chrome")
    web_page.open_page(ShadoDOMLocators.main_url)
    yield web_page
    web_page.driver.quit()


def test_shadow_dom_page(web_page):
    response = requests.get(ShadoDOMLocators.main_url)
    assert response.status_code == 200


# TODO
def test_redirector_message(web_page):
    text_1 = web_page.get_elements(*ShadoDOMLocators.paraps)[0]
    shadow_root_script = "return arguments[0].shadowRoot"
    shadow_root = web_page.driver.execute_script(shadow_root_script, text_1)
    span_element_script = "return arguments[0].querySelector('span')"
    span_element = web_page.driver.execute_script(span_element_script, shadow_root)
    # shadow_element = shadow_root.shadow_root
    # res = shadow_element.find_element(By.XPATH, "//span[@slot='my-text']")
    assert span_element.text == "Let's have some different text!"
