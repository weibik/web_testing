import pytest
import requests
from selenium.webdriver import Keys

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import HorizontalSliderLocators


@pytest.fixture(scope="function")
def web_page():
    web_page = WebPage("Chrome")
    web_page.open_page(HorizontalSliderLocators.main_url)
    yield web_page
    web_page.driver.quit()


def test_horizontal_slider_first_page(web_page):
    response = requests.get(HorizontalSliderLocators.main_url)
    assert response.status_code == 200


def test_slider(web_page):
    assert web_page.get_element(*HorizontalSliderLocators.title).text == "Horizontal Slider"
    slider = web_page.get_element(*HorizontalSliderLocators.slider)
    value = web_page.get_element(*HorizontalSliderLocators.slider_value).text
    assert value == "0"
    num_of_moves = 5
    for i in range(num_of_moves):
        slider.send_keys(Keys.ARROW_RIGHT)
    value = web_page.get_element(*HorizontalSliderLocators.slider_value).text
    expected_value = '2.5'
    assert value == expected_value


def test_maximum_slider_value(web_page):
    slider = web_page.get_element(*HorizontalSliderLocators.slider)
    num_of_moves = 15
    expected_slider_value = '5'
    for i in range(num_of_moves):
        slider.send_keys(Keys.ARROW_RIGHT)
    value = web_page.get_element(*HorizontalSliderLocators.slider_value).text
    assert value == expected_slider_value


def test_minimum_slider_value(web_page):
    slider = web_page.get_element(*HorizontalSliderLocators.slider)
    num_of_moves = 5
    for i in range(num_of_moves):
        slider.send_keys(Keys.ARROW_RIGHT)
    for i in range(num_of_moves * 2):
        slider.send_keys(Keys.ARROW_LEFT)
    value = web_page.get_element(*HorizontalSliderLocators.slider_value).text
    expected_slider_value = '0'
    assert value == expected_slider_value
