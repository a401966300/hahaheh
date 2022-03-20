from selenium.webdriver.common.by import By


class LoginLocator:
    username_loc = (By.ID, 'txtUsername')
    password_loc = (By.ID, 'txtPassword')
    login_btn_loc = (By.CLASS_NAME, 'sso-btn-login')
    logout_text_loc = (By.XPATH, '//*[@id="logout_ok"]')
    wrong_account_passwd_text_loc = (By.XPATH, '/html/body/div[2]/div/div/form/div[2]/span')
    account_login_text_loc = (By.XPATH, '/html/body/div[2]/div/div/form/div[1]/span')
