from time import sleep

import pytest
import requests

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import FramesLocators


@pytest.fixture(scope="function")
def web_page(request):
    web_page = WebPage("Chrome")
    web_page.open_page(FramesLocators.main_url)
    yield web_page
    web_page.driver.quit()


def test_frames_page(web_page):
    response = requests.get(FramesLocators.main_url)
    assert response.status_code == 200


def test_nested_frames(web_page):
    web_page.get_element(*FramesLocators.nested_frames_link).click()
    web_page.wait_for_correct_current_url(FramesLocators.nested_url)
    web_page.driver.switch_to.frame("frame-top")
    assert web_page.check_if_exists(*FramesLocators.nested_left)
    assert web_page.check_if_exists(*FramesLocators.nested_middle)
    assert web_page.check_if_exists(*FramesLocators.nested_right)
    web_page.driver.switch_to.parent_frame()
    assert web_page.check_if_exists(*FramesLocators.nested_bottom)
    web_page.driver.switch_to.frame("frame-bottom")
    bottom_frame = web_page.get_element(*FramesLocators.bottom_inside)
    assert bottom_frame.text == "BOTTOM"


def test_iframe(web_page):
    """
    More complex approach than other tests.
    # TODO Divide into separate functions
    1. Clear text
    2. Set text italic
    3. Set font as tahoma
    4. Enter text and verify it
    5. Click undo
    6. Verify that text is empty
    7. Click redo
    8. Verify that text is as before
    """
    web_page.get_element(*FramesLocators.iframe_link).click()
    web_page.wait_for_correct_current_url(FramesLocators.iframe_url)
    assert web_page.check_if_visible(*FramesLocators.iframe_welcome_screen)
    web_page.change_frame(FramesLocators.iframe_id)
    text_field = web_page.get_element(*FramesLocators.text_area)
    text_field.clear()
    web_page.driver.switch_to.parent_frame()
    web_page.get_element(*FramesLocators.format_button).click()
    web_page.get_element(*FramesLocators.font_option).click()
    web_page.get_element(*FramesLocators.tahoma_font).click()
    web_page.get_element(*FramesLocators.format_button).click()
    web_page.get_element(*FramesLocators.italic_option).click()
    web_page.change_frame(FramesLocators.iframe_id)
    text_field.send_keys(FramesLocators.text_to_send)
    inner_text_field = web_page.get_element(*FramesLocators.inner_text_field)
    entered_text = web_page.get_element(*FramesLocators.entered_text)
    assert entered_text.text == FramesLocators.text_to_send
    font_style = inner_text_field.value_of_css_property("font-style")
    font_family = inner_text_field.value_of_css_property("font-family")
    assert font_style == "italic"
    assert "tahoma" in font_family
    web_page.go_to_parent_frame()
    web_page.get_element(*FramesLocators.format_button).click()
    web_page.get_element(*FramesLocators.format_button).click()
    web_page.change_frame(FramesLocators.iframe_id)
    sleep(2)
    text_field.send_keys(FramesLocators.text_to_send_2)
    entered_text = web_page.get_element(*FramesLocators.entered_text)
    assert entered_text.text == FramesLocators.text_to_send + FramesLocators.text_to_send_2
    web_page.go_to_parent_frame()
    web_page.get_element(*FramesLocators.edit_button).click()
    web_page.get_element(*FramesLocators.undo_option).click()
    web_page.change_frame(FramesLocators.iframe_id)
    entered_text = web_page.get_element(*FramesLocators.entered_text)
    assert entered_text.text == ""
    web_page.go_to_parent_frame()
    web_page.get_element(*FramesLocators.edit_button).click()
    web_page.get_element(*FramesLocators.redo_option).click()
    web_page.change_frame(FramesLocators.iframe_id)
    entered_text = web_page.get_element(*FramesLocators.entered_text)
    assert entered_text.text == FramesLocators.text_to_send + FramesLocators.text_to_send_2

