import unittest
from v4.page.page_login import PageLogin
from selenium import webdriver
import time
from parameterized import parameterized

def get_data():
    return (['15000001111','a19940122','8888','账号不存在'],['15083884232','a1994012','8888','密码错误!'])
url = 'http://localhost'
class TestLogin(unittest.TestCase):

    def setUp(self):
        # 获取页面对象
        self.login = PageLogin()


    @parameterized.expand(get_data())
    def test_login(self,username,password,code,err_info):
        self.login.page_login(username,password,code)
        self.msg = self.login.page_get_error_info()
        try:
            self.assertEqual(self.msg,err_info)
            self.login.page_click_err_btn_ok()
        except AssertionError:
            self.login.page_get_screenshot()


    def tearDown(self):
        self.login.driver.quit()
