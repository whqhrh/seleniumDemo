# -*- coding:utf-8 -*-
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://home.testing-studio.com')
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        # 直接等待
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="ember41"]').click()
        # 显式等待
        WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="ember445"]/div[1]')))
        self.driver.find_element_by_link_text('热门').click()


if __name__ == "__main__":
    pytest.main()
