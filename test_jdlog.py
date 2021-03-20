# -*- coding:utf-8 -*-

import pytest
from selenium import webdriver


class TestJd:
    def setup(self):
        print('\n初始化，打开京东主页')
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.jd.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        pass
        # self.driver.quit()

    def test_jd(self):
        self.driver.find_element_by_css_selector('#ttbar-login > a.link-login').click()
        self.driver.find_element_by_xpath(
            '//*[@id="content"]/div[2]/div[1]/div/div[3]/a').click()
        self.driver.find_element_by_css_selector('#loginname').send_keys('17301370015')
        self.driver.find_element_by_css_selector('#nloginpwd').send_keys('changsi12')


if __name__ == "__main__":
    pytest.main()
