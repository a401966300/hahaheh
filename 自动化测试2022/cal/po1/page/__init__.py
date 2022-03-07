from selenium.webdriver.common.by import By

data = [0,1,2,3,4,5,6,7,8,9]
cal_jiahao = By.CSS_SELECTOR,'#simpleAdd'
cal_sum = By.CSS_SELECTOR,'#simpleEqual'

cal_value = By.CSS_SELECTOR,'#simple{}'.format(data[0])
print(cal_value[1])

cal_text = By.CSS_SELECTOR,'#resultIpt'

