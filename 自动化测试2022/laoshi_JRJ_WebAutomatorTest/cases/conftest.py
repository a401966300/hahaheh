from selenium import webdriver
import pytest
import os
from test_data.url_data import login_url
from pages.login_page import LoginPage
chromedriver_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'chromedriver'))
from time import sleep

driver = None


@pytest.fixture(scope='session')
def handler():
    global driver
    driver = webdriver.Chrome(chromedriver_path)
    driver.maximize_window()
    driver.get(login_url)
    lp = LoginPage(driver)
    yield driver, lp
    driver.quit()


@pytest.fixture()
def refresh_page():
    driver.refresh()
    sleep(3)


def pytest_configure(config):
    markers = ['smoke', 'last']
    for mark in markers:
        config.addinivalue_line('markers', mark)
