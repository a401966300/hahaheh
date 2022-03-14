from v4 import page
from v4.base.base import Base


class PageLogin(Base):
    #base = base()
    # 点击登录链接
    def page_click_login_link(self):
        self.base_click(page.login_link)
    # 输入用户名
    def page_input_username(self,username):
        self.base_input(page.login_username,username)
    #输入密码
    def page_input_password(self,password):
        self.base_input(page.login_password,password)
    #输入验证码
    def page_input_verify_code(self,code):
        self.base_input(page.login_verify_code,code)
    #点击登录按钮
    def page_click_login_btn(self):
        self.base_click(page.login_btn)
    #获取异常提示信息
    def page_get_error_info(self):
        return self.base_get_text(page.login_err_info)
    #点击异常提示框确定按钮
    def page_click_err_btn_ok(self):
        self.base_click(page.login_err_btn_ok)
    #截图
    def page_get_screenshot(self):
        self.base_get_image()
    #判断元素
    def page_login_element_if_exist(self):
        return self.base_is_exist(page.login_link)
    def page_logout_if_exist(self):
        return self.base_is_exist(page.login_logout)
    #安全退出
    def page_logout(self):
        self.base_click(page.login_logout)

    #组合业务方法
    def page_login(self,username,password,code):
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_input_verify_code(code)
        self.page_click_login_btn()


