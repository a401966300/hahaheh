import os
import pytest
from selenium import webdriver
from time import sleep

# print(os.path.join(os.path.dirname(__file__)))
# print(os.path.dirname(__file__))

@pytest.fixture()
def login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://www.baidu.com')
    sleep(3)
    yield driver
    driver.quit()

def test_demo01(login):
    driver = login
    assert driver.title == '百度一下，你就知道'

if __name__ == '__main__':
    args = ['-q','-s','-k','test_practi.py']
    pytest.main(args=args)

