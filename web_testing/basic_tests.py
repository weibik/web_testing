import unittest

from web_testing.basic_page import WebPage
from web_testing.the_internet_elements import TheInternetMainPageLocators


class MainPageTest(unittest.TestCase):
    def setUp(self):
        self.web_page = WebPage("Chrome")

    def tearDown(self):
        self.web_page.driver.quit()

    def test_web_start(self):
        self.web_page.open_page(TheInternetMainPageLocators.main_url)
        element = self.web_page.driver.find_element(*TheInternetMainPageLocators.ab_testing)
        element.click()
        self.assertEqual(self.web_page.driver.current_url, "https://the-internet.herokuapp.com/abtest")
