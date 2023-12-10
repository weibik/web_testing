from time import sleep

import pytest
import requests

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import RedirectionLocators


@pytest.fixture(scope="function")
def web_page():
    web_page = WebPage("Chrome")
    web_page.open_page(RedirectionLocators.main_url)
    yield web_page
    web_page.driver.quit()


def test_redirector_page(web_page):
    response = requests.get(RedirectionLocators.main_url)
    assert response.status_code == 200


def test_redirector_message(web_page):
    web_page.get_element(*RedirectionLocators.redirect_button).click()
    assert web_page.driver.current_url == RedirectionLocators.status_codes_url
    req_list = [RedirectionLocators.req_200, RedirectionLocators.req_301, RedirectionLocators.req_404,
                RedirectionLocators.req_500,]
    req_list_titles = [RedirectionLocators.status_codes_200_title, RedirectionLocators.status_codes_301_title,
                       RedirectionLocators.status_codes_404_title, RedirectionLocators.status_codes_500_title]
    assert len(req_list) == len(req_list_titles)
    for i in range(len(req_list)):
        web_page.wait_for_visibility(*RedirectionLocators.status_codes_info)
        web_page.get_element(*req_list[i]).click()
        web_page.wait_for_visibility(*req_list_titles[i])
        web_page.open_page(RedirectionLocators.status_codes_url)



