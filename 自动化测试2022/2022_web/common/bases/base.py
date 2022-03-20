from common.bases.get_log import logger
from time import sleep

logger = logger()

class Base():

    def __init__(self,driver):
        self.driver = driver

    def search_element(self,loc,msg = ''):
        try:
            logger.info(f'开始查找页面元素:{msg}')
            return self.driver.find_element(*loc)
        except Exception as e:
            logger.error(f'查找页面元素失败:{e}')

    def click_element(self,loc,msg = ''):
        logger.info(f'开始点击页面元素:{msg}')
        self.search_element(loc).click()

    def send_data(self,loc,data,msg = ''):
        logger.info(f'开始向页面元素:{msg}发送数据{data}')
        ele = self.search_element(loc)
        ele.clear()
        ele.send_keys(data)

    def get_element_text(self,loc,msg = ''):
        logger.info(f'获取页面元素文本')
        return self.search_element(loc).text

    def wait(self,sec,msg = ''):
        logger.info(f'{msg},等待:{sec}s')
        sleep(sec)






