from selenium.webdriver.common.by import By

class LoginLocator:
    username_loc = (By.ID,'txtUsername')
    password_loc = (By.ID, 'txtPassword')
    login_btn_loc = (By.CLASS_NAME, 'sso-btn-login')
    logout_text_loc = (By.ID, 'logout_ok')

