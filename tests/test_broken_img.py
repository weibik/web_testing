import pytest
import requests

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import BrokenImagesLocators


@pytest.fixture(scope="function")
def web_page():
    web_page = WebPage("Chrome")
    web_page.open_page(BrokenImagesLocators.main_url)
    yield web_page
    web_page.driver.quit()


def test_images(web_page):
    images = web_page.get_elements_by_tag_name("img")

    for img in images:
        src = img.get_attribute("src")

        if src.endswith((".png", ".jpg", ".jpeg")):
            response = requests.head(src)
            assert response.status_code != 200, f"Broken image found: {src}"
        else:
            print(f"Invalid image format: {src}")
