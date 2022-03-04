#导包
import unittest
import time
from parameterized import parameterized
from v3.page.page_login import PageLogin

data = PageLogin.data

#data = (['15000001111','a19940122','8888'],['15083884232','a1994012','8888'])
#新建测试类
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.login = PageLogin()

    @parameterized.expand(data)
    def test_login(self,username,password,verify_code,text):
        self.login.page_login(username,password,verify_code)
        msg = self.login.page_get_text()
        try:
            self.assertEqual(msg,text)
            time.sleep(3)
            self.login.page_click_err_btn_ok()
        except AssertionError:
            self.login.driver.get_screenshot_as_file('../err_image/error_picture_{}.png'.format(time.strftime('%Y-%m-%d %H-%M-%S')))

    def tearDown(self):
        self.login.driver.quit()
