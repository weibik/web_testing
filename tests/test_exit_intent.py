import pytest
import requests

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import ExitIntentLocators


@pytest.fixture(scope="function")
def web_page():
    web_page = WebPage("Chrome",  "600", "600")
    web_page.open_page(ExitIntentLocators.main_url)
    yield web_page
    web_page.driver.quit()


def test_dynamic_loading_first_page(web_page):
    response = requests.get(ExitIntentLocators.main_url)
    assert response.status_code == 200


# TODO
# def test_modal_window_re_enable(web_page):
#     """ Problematic test. Probably cannot be done via selenium, because it works inside web browser,
#     so you cannot go beyond that. """
    # assert web_page.check_if_exists(*ExitIntentLocators.modal_window)
    # close = web_page.get_element(*ExitIntentLocators.close_button)
    # close.click()
    # web_page.refresh()
    # actions = ActionChains(web_page.driver)
    # actions.move_by_offset(0, -100).perform()
    # wait = WebDriverWait(web_page.driver, 3)
    # assert wait.until(EC.visibility_of_element_located(ExitIntentLocators.modal_window))

