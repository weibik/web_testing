import pytest

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import BasicAuthLocators


# TODO
@pytest.fixture(scope="function")
def web_page():
    web_page = WebPage("Chrome")
    web_page.open_page(BasicAuthLocators.main_url)
    yield web_page
    web_page.driver.quit()


def test(web_page):
    pass

# TODO
