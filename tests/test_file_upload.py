import os
from glob import glob
from time import sleep

import pytest
import requests
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import FileUploadLocators


@pytest.fixture(scope="function")
def web_page(request):
    web_page = WebPage("Chrome")
    web_page.open_page(FileUploadLocators.main_url)
    yield web_page
    web_page.driver.quit()


def test_file_upload_first_page(web_page):
    response = requests.get(FileUploadLocators.main_url)
    assert response.status_code == 200


def test_upload_random_files(web_page):
    files_to_upload = glob(os.path.join(web_page.upload_directory, '*'))
    choose_button = web_page.get_element(*FileUploadLocators.choose_file)
    for file in files_to_upload:
        choose_button.send_keys(file)
    upload_button = web_page.get_element(*FileUploadLocators.upload_button)
    upload_button.click()
    web_page.wait_for_visibility(FileUploadLocators.finish_msg[1])
