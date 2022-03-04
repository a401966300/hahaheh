#encoding=utf-8

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# 鼠标操作及键盘操作
options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.set_window_size(500,500)
sleep(2)
driver.set_window_position(600,540)
sleep(2)
driver.maximize_window()
sleep(1)
aa = driver.find_element_by_link_text('贴吧')
sleep(1)
#ActionChains(driver).context_click().perform()   # 鼠标右键
#sleep(2)
#ActionChains(driver).double_click().perform()   # 鼠标双击
bb = driver.find_element_by_link_text('新闻')
sleep(2)
ActionChains(driver).drag_and_drop(aa,bb).perform()  # 鼠标从一个元素移动到另一个元素
ActionChains(driver).move_to_element('aa').perform()   # 鼠标移动到指定的元素上
sleep(2)
print(driver.title)
driver.quit()
#driver.find_element(By.id,'kw')

driver.find_element_by_link_text('aa').send_keys(Keys.BACKSPACE)  # 删除

keyboard = driver.find_element_by_id('kw')
keyboard.send_keys(Keys.CONTROL,'t')   # 新增窗口
keyboard.send_keys(Keys.SPACE)  #  空格


# 显式等待
from selenium.webdriver.support.wait import WebDriverWait






