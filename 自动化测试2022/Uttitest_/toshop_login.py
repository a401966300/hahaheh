import unittest
from selenium import webdriver
from time import sleep
import time

# 验证网站登录功能


class TestTpshopLogin(unittest.TestCase):


    def setUp(self):
        print('执行SETUP')
        self.url = ''
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def test_login(self):
        driver = self.driver
        driver.find_element_by_link_text('登录').click()
        sleep(2)
        # 定位登录，输入账号密码
        driver.find_element_by_id('username').send_keys('aa')
        driver.find_element_by_id('password').send_keys('115')
        driver.find_element_by_id('verify_code').send_keys('5566')
        driver.find_element_by_css_selector('#login').click()
        # 获取验证码不能为空的提示信息
        result = driver.find_element_by_css_selector('.j_login').text
        try:
            self.assertEqual(result,'验证码不能为空!')
        except AssertionError as f:
            driver.get_screenshot_as_file('./error_img{}.png'.format(time.strftime('%Y-%m-%d %H-%M-%S')))
            #主动抛出异常
            raise

    def test_add_01(self):
        pass


    def tearDown(self):
        print('执行TEARDOWN')
        sleep(2)
        self.driver.quit()




#测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestTpshopLogin))
#suite.addTest(Test01('test_add_01'))
# 执行测试套件
runner = unittest.TextTestRunner()
runner.run(suite)
