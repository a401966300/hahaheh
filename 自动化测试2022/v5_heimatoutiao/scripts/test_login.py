import unittest
import time
from v5_heimatoutiao.log.get_logger import GetLogger
from v5_heimatoutiao.page.page_login import PageLogin
from parameterized import parameterized
from v5_heimatoutiao.tools.get_data import get_json
from v5_heimatoutiao.tools.get_driver import GetDriver
log = GetLogger().get_logger()

# 获取测试用例的数据
datas = get_json('data.json')

class TestLogin(unittest.TestCase):

    driver = None
    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver().get_driver()
        cls.page = PageLogin(cls.driver)
        cls.page.page_click_login_link()

    @parameterized.expand(datas)
    def test_login(self,username,password,code,error_info,makr):
        # 开始登录
        log.info('从这里开始进行登录操作')
        self.page.page_login(username, password, code)
        if makr == 'True':
            try:
                log.info('判断安全退出元素是否存在')
                self.assertTrue(self.page.page_tuichu_is_exist())
                time.sleep(5)
                self.page.page_click_logout()
                time.sleep(5)
                try:
                    self.assertTrue(self.page.page_login_is_exist())
                except Exception as e:
                    log.info('断言失败')
                self.page.page_click_login_link()
            except Exception as e:
                log.info('断言失败')
        else:
            self.msg = self.page.page_get_error_text()
            try:
                self.assertEqual(self.msg,error_info)
            except Exception as e:
                log.error(f'报错信息-{self.msg}-和预期结果-{error_info}-不一致！')
                self.page.base_get_image()
            self.page.page_click_error_btn()

    @classmethod
    def tearDownClass(cls):
        GetDriver().quit_driver()

