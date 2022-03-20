from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime
from run import img_dir_path
import time
from run import logger


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def search_element(self, locator):
        logger.info('开始查找页面元素：{}'.format(locator))
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        logger.info('开始点击页面元素： {}'.format(locator))
        self.search_element(locator).click()

    def send_data(self, locator, data):
        logger.info('开始向页面元素发送数据： {}'.format(locator))
        self.search_element(locator).send_keys(data)

    def wait_element_visible(self, locator, msg=''):
        try:
            now = datetime.now()
            WebDriverWait(self.driver, 20).\
                until(EC.visibility_of_element_located(locator))
            end = datetime.now()
            cost_time = (end - now).total_seconds()
            logger.info('等待元素可见共耗时： {}s'.format(cost_time))
        except Exception as e:
            logger.error(e)

    def get_element_text(self, locator, msg=''):
        self.wait_element_visible(locator, msg)
        return self.search_element(locator).text

    def save_picture(self, msg=''):
        img_path = img_dir_path + '{0}-{1}.png'.format(msg, time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime()))
        try:
            self.driver.save_screenshot(img_path)
            logger.info('截图成功，图片保存路径为：{}'.format(img_path))
        except Exception as e:
            logger.info('截图失败')
            logger.info(e)
