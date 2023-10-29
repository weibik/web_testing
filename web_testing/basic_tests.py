import unittest

from web_testing.basic_page import WebPage
from web_testing.the_internet_elements import TheInternetMainPageLocators
from web_testing.the_internet_elements import AddRemovePageLocators


class MainPageTests(unittest.TestCase):
    def setUp(self):
        self.web_page = WebPage("Chrome")
        self.web_page.open_page(TheInternetMainPageLocators.main_url)

    def tearDown(self):
        self.web_page.driver.quit()

    def test_main_page(self):
        self.assertEqual(self.web_page.driver.current_url, "https://the-internet.herokuapp.com/")
        self.assertEqual(self.web_page.driver.title, "The Internet")

    def test_ab_page(self):
        element_ab_testing = self.web_page.driver.find_element(*TheInternetMainPageLocators.ab_testing_page)
        element_ab_testing.click()
        self.assertEqual(self.web_page.driver.current_url, "https://the-internet.herokuapp.com/abtest")

    def test_add_remove_page(self):
        add_remove_page_hiperlink = self.web_page.driver.find_element(*TheInternetMainPageLocators.add_remove_page)
        add_remove_page_hiperlink.click()
        self.assertEqual(self.web_page.driver.current_url,
                         "https://the-internet.herokuapp.com/add_remove_elements/")


class AddRemoveTests(unittest.TestCase):
    def setUp(self):
        self.web_page = WebPage("Chrome")
        self.web_page.open_page(AddRemovePageLocators.main_url)

    def tearDown(self):
        self.web_page.driver.quit()
