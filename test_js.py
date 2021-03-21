# -*- coding:utf-8 -*-
from time import sleep

from setdown import Fixture


class TestJs(Fixture):
    def test_js_scroll(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('selenium测试')
        # 获取js代码返回值
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        sleep(3)
        # js代码处理向下滑动
        self.driver.execute_script("document.scrollingElement.scrollTop=10000")
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        sleep(5)
        # 获取 网页性能相关数据
        for code in [
            'return document.title', 'return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))
