# -*- coding:utf-8 -*-
import os
from time import sleep

import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip()
    @allure.feature('单击，双击，右键')
    def test_case_click(self):
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        element_click = self.driver.find_element_by_xpath("//input[@value='click me']")
        element_doubleclick = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        element_rightclick = self.driver.find_element_by_xpath("//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_rightclick)
        action.double_click(element_doubleclick)
        sleep(3)
        action.perform()
        sleep(3)

    @pytest.mark.skip()
    @allure.feature('光标移动')
    def test_movetoelement(self):
        self.driver.get('https://www.baidu.com')
        ele = self.driver.find_element_by_css_selector('#s-usersetting-top')
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        sleep(3)
        action.perform()
        sleep(3)

    @allure.feature('拖动到某一个位置')
    def test_dragdrop(self):
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        drag_element = self.driver.find_element_by_id('dragger')
        drop_element = self.driver.find_element_by_xpath('/html/body/div[2]')
        sleep(3)
        action = ActionChains(self.driver)
        # action.drag_and_drop(drag_element,drop_element).perform()
        action.click_and_hold(drag_element).release(drop_element).perform()
        sleep(3)

    @allure.feature('键盘输入')
    def test_keys(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        ele = self.driver.find_element_by_xpath('/html/body/label[1]/input')
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys('username').pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys('tom').pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)


if __name__ == "__main__":
    pytest.main()
    os.system('allure generate ./temp -o ./outputs --clean')
