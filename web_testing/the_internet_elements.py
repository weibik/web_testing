from selenium.webdriver.common.by import By


class TheInternetMainPageLocators:
    main_url = "https://the-internet.herokuapp.com/"
    ab_testing_page = (By.PARTIAL_LINK_TEXT, "A/B Testing")
    add_remove_page = (By.PARTIAL_LINK_TEXT, "Add/Remove Elements")


class AddRemovePageLocators:
    main_url = "https://the-internet.herokuapp.com/add_remove_elements/"
    add_element_button_xpath = (By.XPATH, "//button[contains(text(),'Add Element')]")
    delete_button_xpath = (By.XPATH, "//button[contains(text(),'Delete')]")


class BasicAuthLocators:
    main_url = "https://the-internet.herokuapp.com/basic_auth"


class BrokenImagesLocators:
    main_url = """https://the-internet.herokuapp.com/broken_images"""
