#encoding=utf-8

from selenium import webdriver
from time import sleep
import time


# iframe窗口切换,在一个网页中嵌套了另一个网页表单，比如QQ空间登录页面
def iframe():
    url = 'https://qzone.qq.com/'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    sleep(1)
    driver.switch_to.frame('login_frame')   #括号内填写frame框架的name,id,或者定位到的frame元素
    driver.find_element_by_id('switcher_plogin').click()
    sleep(2)
    driver.find_element_by_id('u').send_keys('55555555555')
    sleep(3)
    driver.quit()
    # 注意，如果存在两个frame框架，在切换到第一个框架后，如果想切换到第二个框架，需要先回到主框架再切换
    #driver.switch_to_default.content()  # 恢复默认页面方法

#iframe()

def chuankou():
    url = 'https://www.baidu.com/'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    sleep(1)
    driver.find_element_by_link_text('贴吧').click()
    sleep(2)
    print(driver.current_window_handle)
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])
    print(driver.current_window_handle)
    sleep(3)
    driver.find_element_by_id('wd1').send_keys('haha')
    sleep(1)
    # 截屏
    driver.get_screenshot_as_file('./image{}.png'.format(time.strftime('%Y-%m-%d %H-%M-%S')))
    driver.quit()
chuankou()



