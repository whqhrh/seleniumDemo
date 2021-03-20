# -*- coding:utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestPostForm():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_form_post(self):
        self.driver.get('https://ceshiren.com/')
        self.driver.find_element_by_xpath('//*[@id="ember5"]/header/div/div/div[2]/span/button[2]').click()
        sleep(5)
        self.driver.find_element_by_id('login-account-name').send_keys('479094092@qq.com')
        self.driver.find_element_by_id('login-account-password').send_keys('changsi12')
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#login-button > span')))
        self.driver.find_element_by_css_selector('#login-button > span').click()
        sleep(5)
