import os
import shutil

import pytest
import requests

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import FileDownloadLocators


@pytest.fixture(scope="function")
def web_page(request):
    web_page = WebPage("Chrome")
    web_page.open_page(FileDownloadLocators.main_url)
    yield web_page
    web_page.driver.quit()


# TODO Test cleans after itself, but only in case of success. I am not sure how to do it, while it fails.
# TODO I can delete contest of a folder, but it would destroy parallel tests.
def test_dynamic_loading_first_page(web_page):
    response = requests.get(FileDownloadLocators.main_url)
    assert response.status_code == 200


def test_file_download(web_page):
    logo = web_page.get_element(*FileDownloadLocators.logo_png)
    logo.click()
    file_name = "Logo.png"
    path = os.path.join(web_page.download_directory, file_name)
    print(f"INSIDE THE TEST: {path}")
    try:
        WebDriverWait(web_page.driver, 5).until(
            lambda x: os.path.exists(path)
        )
        print(f"DOWNLOAD OF THE {file_name} SUCCESSFUL")
    except TimeoutException:
        print(f"Timed out waiting for file to download to {path}")
    delete_file(path)


def delete_file(download_path):
    try:
        os.remove(download_path)
        print(f"File {download_path} deleted successfully.")
    except OSError as e:
        print(f"Error deleting file {download_path}: {e}")
