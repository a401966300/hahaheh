import pytest
from selenium import webdriver
from test_data.login_test_data import login_url
from common.bases.get_log import logger
from pages.login_page import LoginPage

driver = None
logger = logger()
@pytest.fixture(scope='session')
def handle():
    global driver
    logger.info('准备启动浏览器')
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(login_url)
    logger.info('已经打开测试页面')
    lp = LoginPage(driver)
    yield driver,lp
    driver.quit()
    logger.info('\n金融界WEB自动化测试结束')

