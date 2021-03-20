# -*- coding:utf-8 -*-
from selenium import webdriver


class TestWindow():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_window_frame(self):
        self.driver.get('http://www.baidu.com')
