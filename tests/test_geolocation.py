import pytest
import requests

from web_testing.basic_methods import get_current_location, haversine_distance
from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import GeolocationLocators


@pytest.fixture(scope="function")
def web_page(request):
    web_page = WebPage("Chrome")
    web_page.open_page(GeolocationLocators.main_url)
    yield web_page
    web_page.driver.quit()


def test_test_geolocation_first_page(web_page):
    response = requests.get(GeolocationLocators.main_url)
    assert response.status_code == 200


def test_geolocation(web_page):
    assert web_page.get_element(*GeolocationLocators.title).text == "Geolocation"
    web_page.get_element(*GeolocationLocators.where_am_i_button).click()
    web_page.wait_for_visibility(*GeolocationLocators.latitude)
    web_page.wait_for_visibility(*GeolocationLocators.longitude)
    latitude = web_page.get_element(*GeolocationLocators.latitude).text
    longitude = web_page.get_element(*GeolocationLocators.longitude).text
    assert -90 <= float(latitude) <= 90, f"Latitude should be a number between -90 and 90, but it is {latitude}"
    assert -180 <= float(longitude) <= 180, f"Longitude should be a number between -90 and 90, but it is {longitude}"

    online_coordinates = get_current_location()
    if online_coordinates is not None:
        the_internet_coordinates = latitude, longitude
        verify_distance(the_internet_coordinates, online_coordinates)


def verify_distance(cords1, cords2):
    distance = haversine_distance(cords1, cords2)
    maximum_distance = 3.0
    assert distance <= maximum_distance, (f"Provided distance should be less than {maximum_distance}, but it "
                                          f"is {distance}")

