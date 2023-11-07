import pytest

from web_testing.basic_methods import perform_checkbox_action
from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import CheckboxesLocators


@pytest.fixture(scope="function")
def web_page():
    web_page = WebPage("Chrome")
    web_page.open_page(CheckboxesLocators.main_url)
    yield web_page
    web_page.driver.quit()


def test_check_all_checkboxes(web_page):
    checkboxes = web_page.driver.find_elements(*CheckboxesLocators.checkbox)
    perform_checkbox_action(checkboxes, "check")
    for checkbox in checkboxes:
        assert checkbox.is_selected(), "All checkboxes should be checked"


def test_uncheck_all_checkboxes(web_page):
    checkboxes = web_page.driver.find_elements(*CheckboxesLocators.checkbox)
    perform_checkbox_action(checkboxes, "uncheck")
    for checkbox in checkboxes:
        assert not checkbox.is_selected(), "All checkboxes should be unchecked"
