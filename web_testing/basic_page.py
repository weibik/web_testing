from web_testing.web_driver_structure import Webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class WebPage(Webdriver):
    def open_page(self, url):
        self.driver.get(url)

    def get_element_by_link_text(self, link_text):
        return self.driver.find_element(By.LINK_TEXT, link_text)

    def get_element_by_partial_link_text(self, partial_link_text):
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, partial_link_text)

    def get_element_by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def get_element_by_css_selector(self, css_selector):
        return self.driver.find_element(By.CSS_SELECTOR, css_selector)

    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True
