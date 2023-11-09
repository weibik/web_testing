import pytest

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import BasicAuthLocators


@pytest.fixture(scope="function")
def web_page():
    web_page = WebPage("Chrome")
    yield web_page
    web_page.driver.quit()


def test_correct_credentials(web_page):
    web_page.open_page(BasicAuthLocators.main_url_with_good_credentials)
    result = web_page.driver.find_element(*BasicAuthLocators.congratulations)
    assert (f"{result.text}".__contains__("Congratulations"))


def test_incorrect_credentials(web_page):
    web_page.open_page(BasicAuthLocators.main_url_with_wrong_credentials)
    assert not web_page.check_if_exists(*BasicAuthLocators.congratulations)
