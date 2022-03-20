import time
from v5_heimatoutiao import page
from v5_heimatoutiao.base.base import Base

class PageLogin(Base):

    # 点击登录链接按钮
    def page_click_login_link(self):
        self.base_click(page.login_link)
    # 输入账号
    def page_input_username(self,username):
        self.base_input(page.login_username,username)
    # 输入密码
    def page_input_password(self,password):
        self.base_input(page.login_password,password)
    # 输入验证码
    def page_input_code(self,code):
        self.base_input(page.login_verify_code,code)
    # 点击登录
    def page_click_login(self):
        self.base_click(page.login_btn)
        time.sleep(3)
    # 获取弹框信息
    def page_get_error_text(self):
        return self.base_get_text(page.login_err_info)
    # 点击确定按钮
    def page_click_error_btn(self):
        self.base_click(page.login_err_btn_ok)
    # 点击退出按钮
    def page_click_logout(self):
        self.base_click(page.login_logout)
    # 判定安全退出元素是否存在
    def page_tuichu_is_exist(self):
       return self.base_element_is_exist(page.login_logout)
    # 判定登录元素是否存在
    def page_login_is_exist(self):
        return self.base_element_is_exist(page.login_link)
    def page_get_image(self):
        self.base_get_image()
    # 操作方法组合
    def page_login(self,username,passsword,code):
        self.page_input_username(username)
        self.page_input_password(passsword)
        self.page_input_code(code)
        self.page_click_login()




