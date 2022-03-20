from selenium.webdriver.support.wait import WebDriverWait
import time
from v5_heimatoutiao.log.get_logger import GetLogger

log = GetLogger().get_logger()


class Base:

    def __init__(self,driver):
        self.driver = driver

    #查找元素封装
    def base_find_element(self,loc,timeout=20,poll=0.5):
        log.info(f'正在查找{loc}元素')
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(lambda x: x.find_element(*loc))
    # 输入方法封装
    def base_input(self,loc,value):
        el = self.base_find_element(loc)
        el.clear()
        log.info(f'输入{value}')
        el.send_keys(value)
    # 点击方法封装
    def base_click(self,loc):
        log.info(f'正在点击{loc}元素')
        self.base_find_element(loc).click()
    #获取元素文本封装
    def base_get_text(self,loc):
        return self.base_find_element(loc).text
    # 截图
    def base_get_image(self):
        log.info('开始截图')
        self.driver.get_screenshot_as_file('../image/error_{}.png'.format(time.strftime('%Y-%m-%d %H-%M-%S')))
    # 判断元素是否存在
    def base_element_is_exist(self,loc):
        try:
            self.base_find_element(loc)
            return True
        except:
            return False

