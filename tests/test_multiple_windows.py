import pytest
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import MultipleWindowsLocators
from selenium.webdriver.support import expected_conditions as EC, wait


@pytest.fixture(scope="function")
def web_page():
    web_page = WebPage("Chrome")
    web_page.open_page(MultipleWindowsLocators.main_url)
    yield web_page
    web_page.driver.quit()


def test_large_dom_page(web_page):
    response = requests.get(MultipleWindowsLocators.main_url)
    assert response.status_code == 200


def test_large_dom(web_page):
    web_page.wait_for_visibility(*MultipleWindowsLocators.new_window_button, 5)
    current_window = web_page.driver.current_window_handle
    assert len(web_page.driver.window_handles) == 1
    web_page.get_element(*MultipleWindowsLocators.new_window_button).click()
    WebDriverWait(web_page.driver, 5).until(EC.number_of_windows_to_be(2))
    for window_handle in web_page.driver.window_handles:
        if window_handle != current_window:
            web_page.driver.switch_to.window(window_handle)
            break

    assert WebDriverWait(web_page.driver, 5).until(EC.title_is("New Window"))

