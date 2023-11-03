import unittest
import requests

from web_testing.basic_page import WebPage
from web_testing.the_internet_elements import (TheInternetMainPageLocators, BasicAuthLocators, BrokenImagesLocators,
                                               AddRemovePageLocators)


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
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.web_page.open_page(AddRemovePageLocators.main_url)

    def tearDown(self):
        self.web_page.open_page(AddRemovePageLocators.main_url)

    def test_adding_and_removing_element(self):
        add_element_button = self.web_page.driver.find_element(*AddRemovePageLocators.add_element_button_xpath)
        add_element_button.click()
        assert self.web_page.check_if_exists(*AddRemovePageLocators.delete_button_xpath)
        delete_button = self.web_page.driver.find_element(*AddRemovePageLocators.delete_button_xpath)
        delete_button.click()
        self.assertFalse(self.web_page.check_if_exists(*AddRemovePageLocators.delete_button_xpath),
                         "'Delete' button should be not available")
    
    def test_remove_not_added_element(self):
        self.assertFalse(self.web_page.check_if_exists(*AddRemovePageLocators.delete_button_xpath),
                         "'Delete' button should be not available")

    def test_add_and_delete_multiple_elements(self):
        num_of_clicks = 100
        add_element_button = self.web_page.driver.find_element(*AddRemovePageLocators.add_element_button_xpath)
        for i in range(num_of_clicks):
            add_element_button.click()
        delete_buttons = self.web_page.driver.find_elements(*AddRemovePageLocators.delete_button_xpath)
        assert len(delete_buttons) == num_of_clicks


class BasicAuthTests(BaseTestClass):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.web_page.open_page(BasicAuthLocators.main_url)

    def tearDown(self):
        self.web_page.open_page(BasicAuthLocators.main_url)


class BrokenImageTests(BaseTestClass):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.web_page.open_page(BrokenImagesLocators.main_url)

    def tearDown(self):
        self.web_page.open_page(BrokenImagesLocators.main_url)

    def test_images(self):
        images = self.web_page.get_elements_by_tag_name("img")

        for img in images:
            src = img.get_attribute("src")

            if src.endswith((".png", ".jpg", ".jpeg")):
                response = requests.head(src)
                assert response.status_code != 200, f"Broken image found: {src}"
            else:
                print(f"Invalid image format: {src}")
