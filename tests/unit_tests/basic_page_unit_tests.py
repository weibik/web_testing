import pytest
from selenium.webdriver.common.by import By

from web_testing.basic_page import WebPage


@pytest.fixture(scope="function")
def web_page():
    web_page = WebPage("Chrome")
    web_page.open_page("https://www.google.com/")
    web_page.get_element(By.XPATH, "//*[@id='W0wltc']").click()
    yield web_page
    web_page.driver.quit()


def test_open_page(web_page):
    assert web_page.driver.current_url == "https://www.google.com/"


def test_check_if_exists(web_page):
    assert web_page.check_if_exists(By.XPATH, "//div[@class='FPdoLc lJ9FBc']/center"
                                              "/input[@name='btnK']") is True


def test_check_if_visible(web_page):
    assert web_page.check_if_visible(By.XPATH, "//div[@class='FPdoLc lJ9FBc']/center/"
                                               "input[@name='btnK']") is True
