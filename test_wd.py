# -*- coding:utf-8 -*-
from time import sleep

from setdown import Fixture


class TestWindow(Fixture):

    # def setup(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(5)
    #
    # def teardown(self):
    #     self.driver.quit()

    def test_window_frame(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_css_selector('#s-top-loginbtn').click()
        # 打印当前窗口
        print(self.driver.current_window_handle)
        sleep(3)
        self.driver.find_element_by_css_selector(
            '#passport-login-pop-dialog > div > div > div > div.tang-pass-footerBar > a').click()
        sleep(3)
        # 打印当前窗口
        print(self.driver.current_window_handle)
        # 获取所有窗口list
        window = self.driver.window_handles
        print(window)
        # 切换到注册窗口
        self.driver.switch_to.window(window[-1])
        self.driver.find_element_by_css_selector('#TANGRAM__PSP_4__userName').send_keys('17301370015')
        sleep(3)

        # 切回登录窗口
        self.driver.switch_to.window(window[0])
        self.driver.find_element_by_css_selector('#TANGRAM__PSP_11__footerULoginBtn').click()
        sleep(3)
        self.driver.find_element_by_css_selector('#TANGRAM__PSP_11__userName').send_keys('17301370015')
        sleep(5)
