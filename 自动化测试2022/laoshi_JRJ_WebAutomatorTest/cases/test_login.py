from test_data.data_for_login import success_data
from run import logger
import pytest
from test_data.data_for_login import failed_data
from time import sleep
import allure


@allure.epic('金融界WEB自动化测试')
@allure.feature('金融界WEB自动化测试-登录功能测试')
@pytest.mark.usefixtures('refresh_page')
class TestLogin:
    @allure.story('金融界WEB自动化测试-登录功能测试-正向用例测试')
    @allure.title('登录正向用例测试')
    @pytest.mark.last
    def test_login_success(self, handler):
        logger.info('========= 开始执行正向用例 =========')
        handler[1].login(success_data['username'], success_data['password'])
        logger.info('登录操作完成.')
        sleep(3)
        assert handler[1].get_logout_text()
        logger.info('======== 正向用例测试通过 =========')
        handler[1].save_picture('正向用例测试截图')

    @allure.story('金融界WEB自动化测试-登录功能测试-反向用例测试')
    @allure.title('登录反向用例测试')
    @pytest.mark.parametrize('data', failed_data)
    def test_login_failed(self, handler, data):
        logger.info('开始执行反向测试用例：{}'.format(data['name']))
        handler[1].login(data['username'], data['password'])
        logger.info('登录操作完成.')
        sleep(3)
        if data['username'] == '' or data['password'] == '':
            assert handler[1].get_account_login_text() == data['error_msg']
            handler[1].save_picture('账号或密码为空截图')
        else:
            assert handler[1].get_wrong_account_passwd_text() == data['error_msg']
            handler[1].save_picture('账号或密码错误截图')
