import pytest
import requests
from selenium.webdriver.common.by import By

from web_testing.basic_page import WebPage
from web_testing.the_internet_locators import DataTablesLocators


@pytest.fixture(scope="function")
def web_page():
    web_page = WebPage("Chrome")
    web_page.open_page(DataTablesLocators.main_url)
    yield web_page
    web_page.driver.quit()


def test_sortable_data_res_page(web_page):
    response = requests.get(DataTablesLocators.main_url)
    assert response.status_code == 200


def test_sortable_data_headers(web_page):
    table_1 = web_page.get_element(*DataTablesLocators.table_1)

    headers = table_1.find_elements(By.TAG_NAME, 'th')

    expected_headers = ['Last Name', 'First Name', 'Email', 'Due', 'Web Site', 'Action']
    for index, header in enumerate(headers):
        assert header.text == expected_headers[index]


def test_last_name_sort(web_page):
    table_1 = web_page.get_element(*DataTablesLocators.table_1)
    rows = table_1.find_elements(By.TAG_NAME, 'tr')

    last_name_arr = []
    last_name_arr_sorted = []

    for row in rows[1:]:
        cells = row.find_elements(By.TAG_NAME, 'td')
        last_name_arr.append(cells[0].text)

    web_page.get_element(*DataTablesLocators.table_1_last_name).click()
    rows = table_1.find_elements(By.TAG_NAME, 'tr')

    for row in rows[1:]:
        cells = row.find_elements(By.TAG_NAME, 'td')
        last_name_arr_sorted.append(cells[0].text)

    assert last_name_arr_sorted == sorted(last_name_arr)


