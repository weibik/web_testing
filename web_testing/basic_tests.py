import unittest

from web_testing.basic_page import WebPage
from web_testing.the_internet_elements import TheInternetMainPageLocators


class MainPageTest(unittest.TestCase):
    def setUp(self):
        self.web_page = WebPage("Chrome")

    def tearDown(self):
        self.web_page.driver.quit()

    def test_main_page(self):
        self.web_page.open_page(TheInternetMainPageLocators.main_url)
        self.assertEqual(self.web_page.driver.current_url, "https://the-internet.herokuapp.com/")
        self.assertEqual(self.web_page.driver.title, "The Internet")

    def test_ab_page(self):
        self.web_page.open_page(TheInternetMainPageLocators.main_url)
        element_ab_testing = self.web_page.driver.find_element(*TheInternetMainPageLocators.ab_testing_page)
        element_ab_testing.click()
        self.assertEqual(self.web_page.driver.current_url, "https://the-internet.herokuapp.com/abtest")
