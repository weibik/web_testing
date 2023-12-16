import pytest
import requests

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import ShiftingContentLocators


@pytest.fixture(scope="function")
def web_page():
    web_page = WebPage("Chrome")
    web_page.open_page(ShiftingContentLocators.main_url)
    yield web_page
    web_page.driver.quit()


def test_shifting_content_page(web_page):
    response = requests.get(ShiftingContentLocators.main_url)
    assert response.status_code == 200


def test_menu_element(web_page):
    web_page.get_element(*ShiftingContentLocators.menu_element_button).click()
    web_page.wait_for_correct_current_url("https://the-internet.herokuapp.com/shifting_content/menu")
    web_page.wait_for_visibility(*ShiftingContentLocators.portfolio)
    portfolio_size = web_page.get_element(*ShiftingContentLocators.portfolio).size
    refresh_button = web_page.get_element(*ShiftingContentLocators.refresh_button)
    refresh_button.click()
    web_page.wait_for_correct_current_url(ShiftingContentLocators.refreshed_menu_url)
    portfolio_size_after_reload = web_page.get_element(*ShiftingContentLocators.portfolio).size
    # I've checked many different parameters and attributes, but nothing seems to be changing during page refresh.
    assert portfolio_size != portfolio_size_after_reload


def test_image(web_page):
    web_page.get_element(*ShiftingContentLocators.image_button).click()
    web_page.wait_for_correct_current_url("https://the-internet.herokuapp.com/shifting_content/image")
    web_page.wait_for_visibility(*ShiftingContentLocators.image)
    image_default_location = web_page.get_element(*ShiftingContentLocators.image).location
    web_page.get_element(*ShiftingContentLocators.refresh_image_button).click()
    web_page.wait_for_correct_current_url(ShiftingContentLocators.refreshed_img_url)
    image_refreshed_location = web_page.get_element(*ShiftingContentLocators.image).location
    assert image_default_location != image_refreshed_location


def test_list(web_page):
    web_page.get_element(*ShiftingContentLocators.list_button).click()
    web_page.wait_for_correct_current_url("https://the-internet.herokuapp.com/shifting_content/list")
    web_page.wait_for_visibility(*ShiftingContentLocators.list_page_title)
    list_default = web_page.get_element(*ShiftingContentLocators.list_locator)
    web_page.refresh()
    list_after_refresh = web_page.get_element(*ShiftingContentLocators.list_locator)
    assert list_default != list_after_refresh
