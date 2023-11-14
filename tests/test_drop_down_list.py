import pytest
import requests

from selenium.webdriver.support.ui import Select
from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import DropDownListLocators


@pytest.fixture(scope="function")
def web_page():
    web_page = WebPage("Chrome")
    web_page.open_page(DropDownListLocators.main_url)
    yield web_page
    web_page.driver.quit()


def test_drag_and_drop_page(web_page):
    response = requests.get(DropDownListLocators.main_url)
    assert response.status_code == 200


def test_default_option(web_page):
    assert web_page.driver.find_element(*DropDownListLocators.option_disabled)


def test_options(web_page):
    dropdown = web_page.driver.find_element(*DropDownListLocators.drop_down_list)
    select = Select(dropdown)
    select.select_by_visible_text("Option 1")
    assert select.first_selected_option.text == "Option 1", (f"Selected option should be option 1, "
                                                             f"but it is {select.first_selected_option.text}")
    select.select_by_index(2)
    select.select_by_value("2")
    assert select.first_selected_option.text == "Option 2", (f"Selected option should be option 2, "
                                                             f"but it is {select.first_selected_option.text}")


def test_abnormal_option(web_page):
    dropdown = web_page.driver.find_element(*DropDownListLocators.drop_down_list)
    select = Select(dropdown)
    all_values = [option.text for option in select.options]
    assert all_values == ["Please select an option", "1", "2"], f"All values should be 1 and 2, but it is {all_values}"
