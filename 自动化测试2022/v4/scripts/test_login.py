import unittest
from v4.page.page_login import PageLogin
from selenium import webdriver
from v4.base.get_driver import GetDriver
from v4.tool.read_json import read_json
import time
from parameterized import parameterized

def get_data():
    arrs = []
    datas = read_json('write.json')
    for data in datas.values():
        arrs.append((data['a'],data['b'],data['c'],data['d'],data['e']))
        #print(arrs)
    return arrs

class TestLogin(unittest.TestCase):
    #login = None
    @classmethod
    def setUpClass(cls):
        # 获取页面对象
        cls.driver = GetDriver().get_driver()
        cls.login = PageLogin(cls.driver)
        cls.login.page_click_login_link()


    @parameterized.expand(get_data())
    def test_login(self,username,password,code,err_info,result):
        self.login.page_login(username, password, code)
        if result == 'True':
            try:
                self.assertTrue(self.login.page_logout_if_exist())
                time.sleep(3)
                self.login.page_logout()
                time.sleep(3)
                try:
                    self.assertTrue(self.login.page_login_element_if_exist())
                except:
                    self.login.page_get_screenshot()
                self.login.page_click_login_link()
            except:
                self.login.page_get_screenshot()
        else:
            print('从这里开始')
            self.msg = self.login.page_get_error_info()
            try:
                self.assertEqual(self.msg,err_info)
            except AssertionError:
                self.login.page_get_screenshot()
            # 点击异常提示框确定按钮
            self.login.page_click_err_btn_ok()

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        GetDriver().quit_driver()

