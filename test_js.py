# -*- coding:utf-8 -*-
from time import sleep

import pytest

from setdown import Fixture


class TestJs(Fixture):
    @pytest.mark.skip
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

    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        date = "document.getElementById('train_date').removeAttribute('readonly')"
        self.driver.execute_script(date)
        sleep(3)
        date1 = "document.getElementById('train_date').value='2021-12-30'"
        self.driver.execute_script(date1)
        sleep(3)
        print(f"当前日期为：{self.driver.find_element_by_id('train_date').text}......")
        sleep(5)

