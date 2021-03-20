# -*- coding:utf-8 -*-
import os

from selenium import webdriver


class Fixture:
    def setup(self):
        browser = os.getenv("browser")
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
