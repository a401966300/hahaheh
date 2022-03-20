import time
from selenium import webdriver

url = 'http://www.baidu.com'

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(3)
driver.find_element_by_id('kw').send_keys('图片')
driver.find_element_by_id('su').click()
time.sleep(3)
driver.quit()

