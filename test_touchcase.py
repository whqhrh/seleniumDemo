# -*- coding:utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchAction():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touch(self):
        """
        打开chrome
        打开URL:http://www.baidu.com
        向搜索框输入‘selenium测试’
        通过TouchAction点击搜索框
        滑动到底部，点击下一页
        关闭Chrome
        :return:
        """
        self.driver.get('http://www.baidu.com')
        el_input = self.driver.find_element_by_id('kw')
        el_search = self.driver.find_element_by_id('su')
        sleep(3)
        el_input.send_keys('selenium测试')
        action = TouchActions(self.driver)
        action.tap(el_search)
        action.perform()
        sleep(3)
        action.scroll_from_element(el_input, 0, 10000).perform()
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        sleep(5)
