from selenium import webdriver
import time
import json
from selenium.webdriver.support.wait import WebDriverWait

'''
计算机案例
1.采用PO模式的分层思想对页面进行封装
2.编写测试脚本
3.使用参数化传入测试数据
'''
url = 'http://cal.apple886.com/'

class CalBase():

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(url)


    def base_find_element(self,loc,timeout=20,poll=0.5):
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(lambda x: x.find_element(*loc))

    def base_click(self,value):
        self.base_find_element(value).clcik()
    def base_get_sum_value(self,text):
        return self.base_find_element(text).text

    def base_get_image(self):
        self.driver.get_screenshot_as_file('./sum_{}.png'.format(time.strftime('%Y-%m-%d %H-%H-%S')))
