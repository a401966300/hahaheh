#encoding=utf-8

from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
sleep(2)
driver.find_element(By.LINK_TEXT,'贴吧').click()
sleep(3)
#driver.find_element_by_link_text('su').click()
#sleep(5)
driver.close()
#driver.find_element(By.id,'kw')

