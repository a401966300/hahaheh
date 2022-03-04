#encoding=utf-8

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# 键盘操作
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
sleep(1)
aa = driver.find_element_by_id('kw')
sleep(1)
aa.send_keys('selenium')
sleep(2)
aa.send_keys(Keys.CONTROL,'a')
sleep(2)
aa.send_keys(Keys.CONTROL,'x')
sleep(2)
aa.send_keys(Keys.CONTROL,'v')
sleep(2)
driver.find_element_by_id('su').click()
sleep(2)
driver.quit()
#driver.find_element(By.id,'kw')
