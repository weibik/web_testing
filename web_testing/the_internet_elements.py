from selenium.webdriver.common.by import By


class TheInternetMainPageLocators:
    main_url = "https://the-internet.herokuapp.com/"
    ab_testing_page = (By.PARTIAL_LINK_TEXT, "A/B Testing")
