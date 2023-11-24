import pytest

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import AddRemovePageLocators


@pytest.fixture(scope="function")
def web_page():
    web_page = WebPage("Chrome")
    web_page.open_page(AddRemovePageLocators.main_url)
    yield web_page
    web_page.driver.quit()
    

def test_adding_and_removing_element(web_page):
    add_element_button = web_page.driver.find_element(*AddRemovePageLocators.add_element_button_xpath)
    add_element_button.click()
    assert web_page.check_if_exists(AddRemovePageLocators.delete_button_xpath)
    delete_button = web_page.driver.find_element(*AddRemovePageLocators.delete_button_xpath)
    delete_button.click()
    assert not web_page.check_if_exists(
        AddRemovePageLocators.delete_button_xpath), "'Delete' button should be not available"


def test_remove_not_added_element(web_page):
    assert not web_page.check_if_exists(AddRemovePageLocators.delete_button_xpath), \
        "'Delete' button should be not available"


def test_add_and_delete_multiple_elements(web_page):
    num_of_clicks = 100
    add_element_button = web_page.driver.find_element(*AddRemovePageLocators.add_element_button_xpath)
    for i in range(num_of_clicks):
        add_element_button.click()
    delete_buttons = web_page.driver.find_elements(*AddRemovePageLocators.delete_button_xpath)
    assert len(delete_buttons) == num_of_clicks
