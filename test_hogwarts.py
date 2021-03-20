# ''''''# -*- coding:utf-8 -*-
#
# import pytest
# from selenium import webdriver
#
#
# class TestHogwarts():
#     def setup(self):
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         # 隐式等待
#         self.driver.implicitly_wait(5)
#
#     def teardown(self):
#         self.driver.quit()
#
#     def test_hogwarts(self):
#         self.driver.get('https://testerhome.com/')
#         self.driver.find_element_by_link_text('社团').click()
#         self.driver.find_element_by_link_text('郑州软件测试圈').click()
#         self.driver.find_element_by_css_selector('.topic-27544 .title > a').click()
#
#
# if __name__ == "__main__":
#     pytest.main()
# ''''''