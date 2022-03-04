import time
from parameterized import parameterized
import unittest
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from time import sleep

url = 'http://localhost'
data = (['15000001111','a19940122','8888'],['15083884232','a1994012','8888'])
class TestLogin(unittest.TestCase):
    #driver = None
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)
        cls.driver.get(url)
        sleep(2)
        cls.driver.find_element_by_link_text('登录').click()

    @parameterized.expand(data)
    def test_login_username_not_exit(self,x,y,z):
        driver = self.driver
        aa = driver.find_element_by_css_selector('#username')
        aa.clear()
        aa.send_keys(x)
        sleep(1)
        bb = driver.find_element_by_css_selector('#password')
        bb.clear()
        bb.send_keys(y)
        sleep(1)
        cc = driver.find_element_by_css_selector('#verify_code')
        cc.clear()
        cc.send_keys(z)
        sleep(1)
        driver.find_element_by_css_selector('.J-login-submit').click()
        sleep(3)
        msg = driver.find_element_by_css_selector('.layui-layer-content').text
        print('登录提示信息为:',msg)
        try:
            driver.find_element_by_css_selector('.layui-layer-btn0').click()
            self.assertEqual(msg,'账号不存在')

        except AssertionError:
            driver.get_screenshot_as_file('./error_picture{}.png'.format(time.strftime('%Y-%m-%d %H-%M-%S')))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


# suite = unittest.TestSuite()
# #suite.addTest(unittest.makeSuite(TestLogin))
# suite.addTest(TestLogin('test_login_username_not_exit'))
#
# runn = unittest.TextTestRunner()
# runn.run(suite)

# with open('./test_report_{}.html'.format(time.strftime('%Y-%m-%d %H-%M-%S')),'wb') as f:
#     runner = HTMLTestRunner(stream=f,title='测试报告',verbosity=2)
#     runner.run(suite)



