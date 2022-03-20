from common.bases.base import Base
from locators.login_locator import LoginLocator

class LoginPage(Base):
    def login(self,username,password):
        self.send_data(LoginLocator.username_loc,username,'用户名输入框')
        self.send_data(LoginLocator.password_loc, password, '密码输入框')
        self.click_element(LoginLocator.login_btn_loc,'登录按钮')

    def get_logout_text(self):
        return self.get_element_text(LoginLocator.logout_text_loc)

    def get_account_wrong_text(self):
        return self.get_element_text(LoginLocator.logout_text_loc)
