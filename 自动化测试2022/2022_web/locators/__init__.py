from selenium.webdriver.common.by import By

login_link = By.LINK_TEXT,'登录'
login_username = By.ID,'txtUsername'
login_password = By.ID,'txtPassword'
login_btn = By.CSS_SELECTOR,'.sso-btn-login'
login_err_info = By.CSS_SELECTOR,'.layui-layer-content'
login_err_btn_ok = By.CSS_SELECTOR,'.layui-layer-btn0'
login_logout = By.LINK_TEXT,'安全退出'
login_url = 'http://localhost/'