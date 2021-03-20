# -*- coding:utf-8 -*-
from time import sleep

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
        self.driver.find_element_by_css_selector('#s-top-loginbtn').click()
        print(self.driver.current_window_handle)
        sleep(3)
        self.driver.find_element_by_css_selector('#passport-login-pop-dialog > div > div > div > div.tang-pass-footerBar > a').click()
        sleep(3)
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)

