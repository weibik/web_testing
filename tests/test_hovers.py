import random

import pytest
import requests
from selenium.webdriver import ActionChains

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import HoversLocators


@pytest.fixture(scope="function")
def web_page():
    web_page = WebPage("Chrome")
    web_page.open_page(HoversLocators.main_url)
    yield web_page
    web_page.driver.quit()


def test_hovers_first_page(web_page):
    response = requests.get(HoversLocators.main_url)
    assert response.status_code == 200


def test_hovers(web_page):
    avatars = web_page.get_elements(*HoversLocators.avatar)
    actions = ActionChains(web_page.driver)
    hovered_parts = web_page.get_elements(*HoversLocators.hovered_part)
    for i in range(len(avatars)):
        actions.move_to_element(avatars[i]).perform()
        assert hovered_parts[i].is_displayed()
        assert f"user{i+1}" in hovered_parts[i].text


def test_random_hover(web_page):
    avatars = web_page.get_elements(*HoversLocators.avatar)
    hovered_parts = web_page.get_elements(*HoversLocators.hovered_part)

    actions = ActionChains(web_page.driver)
    avatar = random.choice(avatars)
    index = avatars.index(avatar)

    actions.move_to_element(avatar).perform()
    assert hovered_parts[index].is_displayed()
    for i in range(len(avatars)):
        if i == index:
            continue
        assert not hovered_parts[i].is_displayed()

