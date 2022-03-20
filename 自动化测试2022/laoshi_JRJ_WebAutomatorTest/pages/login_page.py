from common.bases.base_page import BasePage
from locators.login_locator import LoginLocator
from test_data.data_for_login import success_data


class LoginPage(BasePage):
    def login(self, username, password):
        self.send_data(LoginLocator.username_loc, username)
        self.send_data(LoginLocator.password_loc, password)
        self.click_element(LoginLocator.login_btn_loc)

    def get_logout_text(self):
        return self.get_element_text(LoginLocator.logout_text_loc, msg='退出文本信息')

    def get_wrong_account_passwd_text(self):
        return self.get_element_text(LoginLocator.wrong_account_passwd_text_loc, msg='账号或密码错误')

    def get_account_login_text(self):
        return self.get_element_text(LoginLocator.account_login_text_loc, msg='账号登录文本信息')
