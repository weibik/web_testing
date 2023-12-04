import pytest
import requests
from selenium.webdriver import DesiredCapabilities

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import JsErrorLocators


@pytest.fixture(scope="function")
def web_page():
    web_page = WebPage("Chrome")
    web_page.open_page(JsErrorLocators.main_url)
    yield web_page
    web_page.driver.quit()


def test_js_error_page(web_page):
    response = requests.get(JsErrorLocators.main_url)
    assert response.status_code == 200


def test_js_error(web_page):
    capabilities = DesiredCapabilities.CHROME
    capabilities['goog:loggingPrefs'] = {'browser': 'ALL'}
    browser_logs = web_page.driver.get_log('browser')
    javascript_errors = [log['message'] for log in browser_logs if log['level'] == 'SEVERE']
    if javascript_errors:
        print("JavaScript onload errors found!")
        for error in javascript_errors:
            assert "TypeError" in error
    else:
        print("No JavaScript onload errors found.")


