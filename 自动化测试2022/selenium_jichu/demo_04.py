#encoding=utf-8

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select

def alert1():
    # 下拉框选择
    url = 'http://www.baidu.com'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    sleep(1)
    element = driver.find_element_by_css_selector('#s-user-name-menu')

    Select(element).select_by_index(1)  # 通过索引
    # Select(element).select_by_value('aa')  # 通过属性值
    # Select(element).select_by_visible_text('上海')  # 通过文本值
    sleep(3)

    # 处理警告框
    at = driver.switch_to.alert
    at.accept()  #  同意
    at.dismiss()   # 取消
    at.text  # 弹出框的文本信息



# 滚动条操作，通过调用JS脚本来控制
def js1():
    url = 'http://www.baidu.com'
    js = 'window.scrollTo(0,1000)'   # 0：左边距  1000：垂直边距
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    driver.find_element_by_id('kw').send_keys('selenium')
    sleep(2)
    driver.find_element_by_id('su').click()
    sleep(3)
    driver.execute_script(js)
    sleep(2)
    driver.quit()

js1()




