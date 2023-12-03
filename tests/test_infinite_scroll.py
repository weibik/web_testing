import time

import pytest
import requests

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import InfiniteScrollLocators


@pytest.fixture(scope="function")
def web_page():
    web_page = WebPage("Chrome")
    web_page.open_page(InfiniteScrollLocators.main_url)
    yield web_page
    web_page.driver.quit()


def test_infinite_scroll_page(web_page):
    response = requests.get(InfiniteScrollLocators.main_url)
    assert response.status_code == 200


def test_infinite_scroll(web_page):
    max_scrolls = 10
    scroll_count = 0

    while scroll_count < max_scrolls and scroll_to_bottom(web_page):
        scroll_count += 1


def scroll_to_bottom(web_page: WebPage):
    """
    Function, which scrolls to the bottom of the document and returns True if new height is bigger than the old one.

    Args:
        web_page: web page instance

    Returns: true if page was successfully scrolled down

    """

    initial_height = web_page.driver.execute_script("return document.body.scrollHeight")
    web_page.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = web_page.driver.execute_script("return document.body.scrollHeight")
    return new_height > initial_height
