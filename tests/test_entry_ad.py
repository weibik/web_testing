import pytest
import requests

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import EntryAdLocators


@pytest.fixture(scope="function")
def web_page():
    web_page = WebPage("Chrome")
    web_page.open_page(EntryAdLocators.main_url)
    yield web_page
    web_page.driver.quit()


def test_dynamic_loading_first_page(web_page):
    response = requests.get(EntryAdLocators.main_url)
    assert response.status_code == 200


# Tests fail, because modal window does not appear every time
def test_modal_window_re_enable(web_page):
    assert web_page.check_if_exists(*EntryAdLocators.modal_window)
    close_button = web_page.get_element(*EntryAdLocators.close_button)
    close_button.click()
    assert not web_page.check_if_exists(*EntryAdLocators.modal_window)
    re_enable_button = web_page.get_element(*EntryAdLocators.re_enable_button)
    re_enable_button.click()
    web_page.refresh()
    assert web_page.check_if_exists(*EntryAdLocators.modal_window)


def test_modal_window_refresh(web_page):
    assert web_page.check_if_exists(*EntryAdLocators.modal_window)
    close_button = web_page.get_element(*EntryAdLocators.close_button)
    close_button.click()
    assert not web_page.check_if_exists(*EntryAdLocators.modal_window)
    web_page.refresh()
    assert not web_page.check_if_exists(*EntryAdLocators.modal_window)
