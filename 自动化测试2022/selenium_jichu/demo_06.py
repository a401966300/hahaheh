#encoding=utf-8

from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.support.select import Select



# COOKIE
def chuankou():
    url = 'https://www.baidu.com/'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    sleep(1)
    # 首先手动登录百度，然后通过F12获取COOKIE，然后添加COOKIE，刷新就可以跳过登录
    #print('当前COOKIES:',driver.get_cookies())   #获取所有COOKIES  driver.get_cookie() 获取注定COOKIE
    driver.add_cookie({'name':'BDUSS','value':'J0NWZ5SjQ1LTEzU1phUTl1Q0xJM1NteGlkODVFcEdsRW1ma1pVR0NHcVA3RU5pSUFBQUFBJCQAAAAAAAAAAAEAAAAS6pEi2uCMqIyo7OGbUsW1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI9fHGKPXxxiMW'})  # 添加COOKIE
    sleep(2)
    print('添加的COOKIE为:', driver.get_cookie('BDUSS'))
    driver.refresh()
    sleep(3)
    #driver.quit()
chuankou()



