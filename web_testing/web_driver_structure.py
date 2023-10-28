from selenium import webdriver


class Webdriver:
    def __init__(self, browser_type):
        if browser_type == "Chrome":
            self.driver = webdriver.Chrome()
        elif browser_type == "Edge":
            self.driver = webdriver.Edge()
        else:
            print(f"TYPE: {browser_type}")
            raise ValueError("Invalid browser type. Supported browsers: 'Chrome', 'Edge'.")
        self.setup_web_driver_size()

    def setup_web_driver_size(self):
        screen_width = self.driver.execute_script("return window.screen.width;")
        screen_height = self.driver.execute_script("return window.screen.height;")
        self.driver.set_window_size(screen_width, screen_height)
        self.driver.maximize_window()
