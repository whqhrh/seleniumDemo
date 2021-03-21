# -*- coding:utf-8 -*-
from time import sleep

from setdown import Fixture


class TestJs(Fixture):
    def test_js_scroll(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('selenium测试')
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        sleep(3)
        self.driver.execute_script("return document.scrollingElement.scrollTop=10000")
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        sleep(5)
