from pages.login_page import LoginPage
from test_data.login_test_data import success_data,failed_data
from common.bases.get_log import logger

logger = logger()
class TesttLogin:


    def test_login_sucess(self,handle):

        handle[1].login(success_data['username'],success_data['password'])
        handle[1].wait(5,'正在登录页面')
        assert handle[1].get_logout_text() == success_data['msg']
        logger.info('正向用例通过')


