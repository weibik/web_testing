import pytest

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import ContextMenuLocators


@pytest.fixture(scope="function")
def web_page():
    web_page = WebPage("Chrome")
    web_page.open_page(ContextMenuLocators.main_url)
    yield web_page
    web_page.driver.quit()

    def test_context_menu(web_page):
        web_page.get_element_by_xpath(ContextMenuLocators.context_menu)
        pass

# TODO
