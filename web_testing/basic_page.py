from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_testing.web_driver_structure import Webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class WebPage(Webdriver):
    def open_page(self, url):
        self.driver.get(url)

    def get_element(self, *args):
        return self.driver.find_element(*args)

    def get_elements(self, *args):
        return self.driver.find_elements(*args)

    def get_element_by_id(self, element_id):
        return self.driver.find_element(By.ID, element_id)

    def get_element_by_link_text(self, link_text):
        return self.driver.find_element(By.LINK_TEXT, link_text)

    def get_element_by_partial_link_text(self, partial_link_text):
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, partial_link_text)

    def get_element_by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def get_element_by_css_selector(self, css_selector):
        return self.driver.find_element(By.CSS_SELECTOR, css_selector)

    def get_elements_by_tag_name(self, tag_name):
        return self.driver.find_elements(By.TAG_NAME, tag_name)

    def check_if_exists(self, locator_type, locator):
        try:
            self.driver.find_element(locator_type, locator)
        except NoSuchElementException:
            return False
        return True

    def check_if_visible(self, locator_type, locator, timeout=10):
        try:
            element_present = EC.visibility_of_element_located((locator_type, locator))
            WebDriverWait(self.driver, timeout).until(element_present)
        except (TimeoutException, NoSuchElementException):
            return False
        return True

    def refresh(self):
        self.driver.refresh()

    def wait(self, amount_of_time: int = 5):
        self.driver.implicitly_wait(amount_of_time)

    def wait_for_visibility(self, locator):
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )
