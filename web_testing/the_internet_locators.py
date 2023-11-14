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
    main_url_with_good_credentials = "https://admin:admin@the-internet.herokuapp.com/basic_auth"
    main_url_with_wrong_credentials = "https://admin:user@the-internet.herokuapp.com/basic_auth"
    congratulations = (By.XPATH, "//*[contains(text(),'Congratulations')]")


class BrokenImagesLocators:
    main_url = "https://the-internet.herokuapp.com/broken_images"


class ChallengingDOMLocators:
    main_url = "https://the-internet.herokuapp.com/challenging_dom"


class CheckboxesLocators:
    main_url = "https://the-internet.herokuapp.com/checkboxes"
    checkbox = (By.XPATH, "//input[@type='checkbox']")


class ContextMenuLocators:
    main_url = "https://the-internet.herokuapp.com/context_menu"
    context_menu = (By.XPATH, "//*[@id='hot-spot]")


class DigestAuthenticationLocators:
    main_url = "https://the-internet.herokuapp.com/digest_auth"
    context_menu = ""


class DissapearingElementsLocators:
    main_url = "https://the-internet.herokuapp.com/disappearing_elements"
    home_button = (By.XPATH, "//a[contains(text(),'Home')]")


class DragAndDropLocators:
    main_url = "https://the-internet.herokuapp.com/drag_and_drop"
    draggable_a = (By.XPATH, "//div[@id='column-a']")
    draggable_b = (By.XPATH, "//div[@id='column-b']")


class DropDownListLocators:
    main_url = "https://the-internet.herokuapp.com/dropdown"
    drop_down_list = (By.ID, "dropdown")
    option_disabled = (By.XPATH, "//select[@id='dropdown']/option[@disabled='disabled']")
    option_one = (By.XPATH, "//select[@id='dropdown']/option[@value='1']")
    option_two = (By.XPATH, "//select[@id='dropdown']/option[@value='2']")
