from selenium.webdriver.common.by import By

login_link = By.LINK_TEXT,'登录'
login_username = By.ID,'username'
login_password = By.ID,'password'
login_verify_code = By.ID,'verify_code'
login_btn = By.CSS_SELECTOR,'.J-login-submit'
login_err_info = By.CSS_SELECTOR,'.layui-layer-content'
login_err_btn_ok = By.CSS_SELECTOR,'.layui-layer-btn0'
login_logout = By.LINK_TEXT,'安全退出'
login_url = 'http://localhost/'