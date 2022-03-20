from selenium import webdriver
from v5_heimatoutiao.page import page_login

class GetDriver:

    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver == None:
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.get(page_login.page.login_url)
            return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None



