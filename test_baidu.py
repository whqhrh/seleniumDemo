# -*- coding:utf-8 -*-
import pytest
from selenium import webdriver


class TestSearch:
    def setup(self):
        self.driver= webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')

    def test_search(self):
        self.driver.find_element_by_css_selector('#kw').send_keys('霍格沃兹测试学院')
        self.driver.find_element_by_css_selector('#su').click()

if __name__ == "__main__":
    pytest.main()