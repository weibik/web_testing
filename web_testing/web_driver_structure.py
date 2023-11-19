import os
from selenium import webdriver


class Webdriver:
    def __init__(self, browser_type, width: str = "max", height: str = "max"):
        self.driver = None
        project_directory = os.path.dirname(os.path.abspath(__file__))
        self.download_directory = os.path.join(project_directory, "downloads")
        if browser_type == "Chrome":
            self.initialize_chrome_driver(self.download_directory)
        elif browser_type == "Edge":
            self._initialize_edge_driver(self.download_directory)
        else:
            raise ValueError(f"Invalid browser type: {browser_type}. Supported browsers: 'chrome', 'edge'")
        self.setup_web_driver_size(width, height)

    def setup_web_driver_size(self, width: str, height: str):
        if height == "max" and width == "max":
            screen_height = self.driver.execute_script("return window.screen.height;")
            screen_width = self.driver.execute_script("return window.screen.width;")
            self.driver.maximize_window()
            self.driver.set_window_size(screen_width, screen_height)
        else:
            self.driver.set_window_size(width, height)

    def initialize_chrome_driver(self, download_dir):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": download_dir
        })
        self.driver = webdriver.Chrome(options=chrome_options)

    def _initialize_edge_driver(self, download_dir):
        edge_options = webdriver.EdgeOptions()
        edge_options.add_experimental_option("prefs", {
            "download.default_directory": download_dir
        })
        self.driver = webdriver.Edge(options=edge_options)