from enum import Enum
from automationemailverifier.pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class ResultOptions(Enum):
    OK_STATUS = "Ok, Advice: Safe to send"
    UNVERIFIABLE_STATUS = "Unverifiable, Advice: Risky to send"
    BAD_STATUS = "Bad, Advice: Do not send"

class EmailVerifier(BasePage):
    LOGIN_BUTTON = (By.LINK_TEXT, "Login")
    ENTER_EMAIL = (By.ID, "Email")
    ENTER_PASSWORD = (By.ID, "Password")
    SIGN_IN_BUTTON = (By.CLASS_NAME, "btn-custom")
    EMAIL_FIELD = (By.ID, "contactDomain")
    VERIFY_BUTTON = (By.ID, "btnFindEmail")
    RESULT_BOX = (By.CLASS_NAME, "boxVerifyResult")


    login_email = "demo@sopro.io"
    login_password = "Demo123!"

    def login(self):
        login = self.driver.find_element(*self.LOGIN_BUTTON)
        login.click()

    def email_enter(self, mail):
        email_tag = self.driver.find_element(*self.ENTER_EMAIL)
        email_tag.send_keys(mail)

    def clear_email(self):
        email_clear = self.driver.find_element(*self.EMAIL_FIELD)
        email_clear.clear()

    def password_enter(self, password):
        password_tag = self.driver.find_element(*self.ENTER_PASSWORD)
        password_tag.send_keys(password)

    def click_sign_in(self):
        sign_in = self.driver.find_element(*self.SIGN_IN_BUTTON)
        sign_in.click()

    def email_field(self, email):
        email_field = self.driver.find_element(*self.EMAIL_FIELD)
        email_field.send_keys(email)

    def verify(self):
        verify_button = self.driver.find_element(*self.VERIFY_BUTTON)
        verify_button.click()

    def check_reult(self):
        check_reult_box = self.driver.find_element(*self.RESULT_BOX)
        status = check_reult_box.find_element(By.TAG_NAME, "h1").text
        print(status)
        #advice = check_reult_box.find_element(By.TAG_NAME, "p").text

        if status == "Ok":
            return ResultOptions.OK_STATUS
        elif status == "Bad":
            return ResultOptions.BAD_STATUS
        elif status == "Unverifiable":
            return ResultOptions.UNVERIFIABLE_STATUS

    def sign_in(self):
       self.login()
       self.email_enter(self.login_email)
       self.password_enter(self.login_password)
       self.click_sign_in()
