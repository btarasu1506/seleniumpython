import time
import main
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager # type: ignore

import pytest
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys


class MainTestCases():
    def __init__(self):
        self.driver = None

    def setup_method(self, method):
        options = Options()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        #self.driver = webdriver.Firefox(service=Service(ChromeDriverManager().install()), options=options)

    def url(self):
        self.driver.get("https://www.neuralnine.com/")
        self.driver.maximize_window()

    def select_book(self):
        links = self.driver.find_elements("xpath", "//a[@href]")
        for link in links:
            print(link.get_attribute("innerHTML"))
            if "Books" in link.get_attribute("innerHTML"):
                link.click()
                break
