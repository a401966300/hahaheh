'''
页面对象编写技巧：
   类名：使用大驼峰将模块名称抄进来，有下划线去掉下划线
   方法：根据业务需求每个操作步骤单独封装一个方法
        方法名：page_xxx
'''
import time
from parameterized import parameterized
import unittest
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from time import sleep

url = 'http://localhost'
class PageLogin():
    data = (['15000001111', 'a19940122', '8888','账号不存在'], ['15083884232', 'a1994012', '8888','密码错误!'])
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    # 点击登录链接
    def page_click_login_link(self):
        self.driver.find_element_by_link_text('登录').click()
    # 输入用户名
    def page_input_username(self,username):
        self.driver.find_element_by_id('username').send_keys(username)
    #输入密码
    def page_input_password(self,password):
        self.driver.find_element_by_css_selector('#password').send_keys(password)
    #输入验证码
    def page_input_verify_code(self,verify_code):
        self.driver.find_element_by_css_selector('#verify_code').send_keys(verify_code)
    #点击登录
    def page_click_login_btn(self):
        self.driver.find_element_by_css_selector('.J-login-submit').click()
    #获取异常提示信息
    def page_get_text(self):
        return self.driver.find_element_by_css_selector('.layui-layer-content').text
    #点击提示框确定按钮
    def page_click_err_btn_ok(self):
        self.driver.find_element_by_css_selector('.layui-layer-btn0').click()

    #组装登录业务方法，给业务层调用
    def page_login(self,username,password,verify_code):
        self.page_click_login_link()
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_input_verify_code(verify_code)
        self.page_click_login_btn()
