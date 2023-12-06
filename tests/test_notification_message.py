import logging

import pytest
import requests

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import NotificationMessage


@pytest.fixture(scope="function")
def web_page():
    web_page = WebPage("Chrome")
    web_page.open_page(NotificationMessage.main_url)
    yield web_page
    web_page.driver.quit()


def test_notification_message_page(web_page):
    response = requests.get(NotificationMessage.main_url)
    assert response.status_code == 200


def test_notification_message(web_page):
    num_of_tests = 3
    for i in range(num_of_tests):
        web_page.get_element(*NotificationMessage.reload_message_button).click()
        web_page.wait_for_visibility(*NotificationMessage.message)
        message = web_page.get_element(*NotificationMessage.message)
        message_list = ["Action unsuccesful, please try again", "Action successful"]
        print(f"Message {i} -> {message.text}\n")
        is_valid_msg = any(item in message.text for item in message_list)
        assert is_valid_msg


