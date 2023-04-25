import unittest
from selenium import webdriver
from automationemailverifier.pages.EmailVerifier import EmailVerifier
from automationemailverifier.pages.EmailVerifier import ResultOptions

class TestEmailVerifier(unittest.TestCase):


    def setUp(self) -> None:
        baseUrl = "https://sopro-toolset.azurewebsites.net/email-verifier"

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(baseUrl)
        self.emailVerifier = EmailVerifier(self.driver)


    def tearDown(self):
        self.driver.quit()
        # log out

    def test_email_verifier_ok(self):
        email = "elena@hotmail.com"

        self.emailVerifier.sign_in()
        self.emailVerifier.email_field(email)
        self.emailVerifier.verify()
        self.emailVerifier.driver.implicitly_wait(5)

        assert self.emailVerifier.check_reult().value == ResultOptions.OK_STATUS.value

    def test_email_verifier_bad(self):
        email = "elena@mail.hive.co"

        self.emailVerifier.sign_in()
        self.emailVerifier.email_field(email)
        self.emailVerifier.verify()
        self.emailVerifier.driver.implicitly_wait(5)
        assert self.emailVerifier.check_reult().value == ResultOptions.BAD_STATUS.value

    def test_email_verifier_unverifiable(self):
        email = "zuck@fb.com"

        self.emailVerifier.sign_in()
        self.emailVerifier.email_field(email)
        self.emailVerifier.verify()
        self.emailVerifier.driver.implicitly_wait(5)
        assert self.emailVerifier.check_reult().value == ResultOptions.UNVERIFIABLE_STATUS.value
