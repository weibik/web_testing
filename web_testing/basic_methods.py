import socket
from math import radians, sin, cos, atan2, sqrt

import requests

from selenium.webdriver.remote.webelement import WebElement


def perform_checkbox_action(checkboxes: list[WebElement] | WebElement, action: str) -> None:
    """
    Checks or unchecks all provided fields in checkboxes.
    Args:
        checkboxes: Elements possible to check/uncheck
        action: Check/uncheck checkboxes

    Returns:

    """
    assert action in ["check", "uncheck"]
    for checkbox in checkboxes:
        if (not checkbox.is_selected() and action == "check") or (checkbox.is_selected() and action == "uncheck"):
            checkbox.click()


def get_public_ip():
    """  Return the public IP address using a socket. """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))  # Connect to Google's public DNS server
    ip_address = s.getsockname()[0]
    s.close()

    return ip_address


def get_coordinates_from_ip(ip_address):
    """  Use ipinfo.io to get location information based on the IP address. """
    url = f"http://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    data = response.json()

    if "loc" in data:
        # Extract latitude and longitude from the response
        latitude, longitude = map(float, data["loc"].split(","))
        return latitude, longitude
    else:
        return None


def get_current_location():
    """ Get current location based on ip address. """
    ip_address = get_public_ip()

    if ip_address:
        coordinates = get_coordinates_from_ip(ip_address)
        if coordinates:
            return coordinates

    return None


def haversine_distance(coord1, coord2):
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1, lon1 = map(radians, coord1)
    lat2, lon2 = map(radians, coord2)

    # Differences in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Distance in kilometers
    distance = R * c

    return distance
