import unittest

from web_testing.basic_page import WebPage
from web_testing.the_internet_elements import TheInternetMainPageLocators
from web_testing.the_internet_elements import AddRemovePageLocators


class BaseTestClass(unittest.TestCase):
    web_page = None

    @classmethod
    def setUpClass(cls):
        cls.web_page = WebPage("Chrome")

    @classmethod
    def tearDownClass(cls):
        cls.web_page.driver.quit()


class MainPageTests(BaseTestClass):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.web_page.open_page(TheInternetMainPageLocators.main_url)

    def tearDown(self):
        self.web_page.open_page(TheInternetMainPageLocators.main_url)

    def test_main_page(self):
        self.assertEqual(self.web_page.driver.current_url, "https://the-internet.herokuapp.com/")
        self.assertEqual(self.web_page.driver.title, "The Internet")

    def test_ab_page(self):
        element_ab_testing = self.web_page.driver.find_element(*TheInternetMainPageLocators.ab_testing_page)
        element_ab_testing.click()
        self.assertEqual(self.web_page.driver.current_url, "https://the-internet.herokuapp.com/abtest")

    def test_add_remove_page(self):
        add_remove_page_hyperlink = self.web_page.driver.find_element(*TheInternetMainPageLocators.add_remove_page)
        add_remove_page_hyperlink.click()
        self.assertEqual(self.web_page.driver.current_url,
                         "https://the-internet.herokuapp.com/add_remove_elements/")


class AddRemovePageTests(BaseTestClass):
    def setUpClass(self):
        super().setUpClass()
        self.web_page.open_page(AddRemovePageLocators.main_url)

    def test_adding_element(self):
        add_element_button = self.web_page.driver.find_element(*AddRemovePageLocators.add_element_button)
        add_element_button.click()

    def test_removing_element(self):
        pass
    
    def test_remove_not_added_element(self):
        pass

    def add_multiple_elements(self):
        pass

    def delete_multiple_elements(self):
        pass


