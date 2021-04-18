# -*- coding: utf-8 -*-
# @Time:2021/4/16 20:42
# @Author:WangHQ
# @File:test_demo.py
import os
from time import sleep

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

curpath = os.path.dirname(os.path.realpath(__file__))
yamlpath = os.path.join(curpath, "data\cookie.yaml")


class TestWework:

    def test_Wework(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("menu_contacts").click()
        cookies = self.driver.get_cookies()
        with open(yamlpath, "w", encoding="utf-8") as f:
            yaml.dump(cookies, f)

    def test_cookie(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688850577087676'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'fUQ5UWq79HyCNzUMAe8iKnPprjjyhaRdKSm2syo4ahYxA9uGH2bh9AsPcQ_2pA7drUPtW1GRD4DosooWhVz6cSFmM9cVteR3mmRDJXRgjPDNFuw6004gcH9gRYMIlKhWYRoLZUr3Gj4w9wpPJHnBcojjMCSGGBit-QteKp0gtfe6mVforoJ_o3j-Zg-1pHsEwqmKORqunqT2ynHK3P1vPy44vZKSJ0c5jUi-409s1krh3pyOVBRwcBRTh2w8y4Zfas3ABmSWX_s5UkDy5u5gnw'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688850577087676'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/',
             'secure': False, 'value': '1970324961442635'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'w6i_0_jUMHQ-kyRPCl6-ipTj7btD2_CXdh1puDn6RP3h7qOVwPbffCF9YthPMM-6'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a903382'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/',
             'secure': False, 'value': ''},
            {'domain': '.qq.com', 'expiry': 1618661424, 'httpOnly': False, 'name': '_gat', 'path': '/',
             'secure': False, 'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1618661219'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '1175890803416358'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1618692754, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '2h3jnbj'},
            {'domain': '.qq.com', 'expiry': 1618747772, 'httpOnly': False, 'name': '_gid', 'path': '/',
             'secure': False, 'value': 'GA1.2.1538019077.1618580169'},
            {'domain': '.qq.com', 'expiry': 1681733372, 'httpOnly': False, 'name': '_ga', 'path': '/',
             'secure': False, 'value': 'GA1.2.30810544.1618580169'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1650116168, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '2630697925'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1650197219, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
             'value': '1618581580,1618582908,1618616216,1618661219'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1621253375, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/',
             'secure': False, 'value': 'fc422545f6c4261a6b065e4673bb346cda2d9c4374dc7fae1d910bc71f96b8e7'},
            {'domain': '.qq.com', 'expiry': 2147483649, 'httpOnly': False, 'name': 'RK', 'path': '/',
             'secure': False, 'value': 'EMLJBYtLXe'}]
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        sleep(5)
        self.driver.close()

    def test_cookie2(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        with open(yamlpath, encoding="utf-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element_by_css_selector("#menu_contacts > span").click()
        # 隐式等待
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_link_text("添加成员").click()
        # 直接等待
        sleep(3)
        self.driver.find_element_by_id("username").send_keys("测试123")
        sleep(3)
        self.driver.find_element_by_css_selector("#memberAdd_english_name").send_keys("123")
        sleep(3)
        self.driver.find_element_by_css_selector("#memberAdd_acctid").send_keys("test123")
        sleep(3)
        self.driver.find_element_by_css_selector("#memberAdd_phone").send_keys("13513935689")
        sleep(3)
        self.driver.find_element_by_link_text("保存").click()
        sleep(3)
        self.driver.find_element_by_xpath("//*[@id='menu_index']/span").click()
        sleep(3)
        self.driver.find_element_by_xpath("//*[@id='menu_contacts']/span").click()
        sleep(3)
        a = self.driver.find_element_by_xpath("//*[@id='member_list']/tr[1]/td[2]")
        assert "测试123" == a.text


if __name__ == "__main__":
    pytest.main(['-vs', 'test_demo.py'])
