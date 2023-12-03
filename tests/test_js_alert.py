import pytest
import requests

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import JsAlertsLocators


@pytest.fixture(scope="function")
def web_page():
    web_page = WebPage("Chrome")
    web_page.open_page(JsAlertsLocators.main_url)
    yield web_page
    web_page.driver.quit()


def test_js_alerts_page(web_page):
    response = requests.get(JsAlertsLocators.main_url)
    assert response.status_code == 200


def test_alert(web_page):
    trigger_alert = web_page.get_element(*JsAlertsLocators.alert_trigger)
    trigger_alert.click()
    alert = web_page.driver.switch_to.alert
    assert alert.text == "I am a JS Alert"
    alert.accept()
    assert web_page.get_element(*JsAlertsLocators.result).text == "You successfully clicked an alert"


def test_confirm_accept(web_page):
    trigger_confirm = web_page.get_element(*JsAlertsLocators.confirm_trigger)
    trigger_confirm.click()
    alert = web_page.driver.switch_to.alert
    assert alert.text == "I am a JS Confirm"
    alert.accept()
    assert web_page.get_element(*JsAlertsLocators.result).text == "You clicked: Ok"


def test_confirm_dismiss(web_page):
    trigger_confirm = web_page.get_element(*JsAlertsLocators.confirm_trigger)
    trigger_confirm.click()
    alert = web_page.driver.switch_to.alert
    assert alert.text == "I am a JS Confirm"
    alert.dismiss()
    assert web_page.get_element(*JsAlertsLocators.result).text == "You clicked: Cancel"


def test_prompt(web_page):
    trigger_prompt = web_page.get_element(*JsAlertsLocators.prompt_trigger)
    trigger_prompt.click()
    alert = web_page.driver.switch_to.alert
    assert alert.text == "I am a JS prompt"
    message = "Test information with different chars @9!"
    alert.send_keys(message)
    alert.accept()
    assert web_page.get_element(*JsAlertsLocators.result).text == f"You entered: {message}"
