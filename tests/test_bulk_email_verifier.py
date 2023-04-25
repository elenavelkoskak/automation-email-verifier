import unittest
from selenium import webdriver
from automationemailverifier.pages.BulkEmailVerifier import BulkEmailVerifier
from automationemailverifier.pages.EmailVerifier import EmailVerifier

class TestBulkEmailVerifier(unittest.TestCase):

    def setUp(self) -> None:
        baseUrl = "https://sopro-toolset.azurewebsites.net/email-verifier/bulk"

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(baseUrl)
        self.emailVerifier = EmailVerifier(self.driver)
        self.bulkEmailVerifier = BulkEmailVerifier(self.driver)

    def tearDown(self):
        self.driver.quit()
        # log out

    def test_bulk_verifier(self):
        path_to_file = "C:/Users/Home/PycharmProjects/automation-email-verifier/automationemailverifier/data"
        file_name = "Email_Contacts_Three_Records.csv"
        email_csv_file = f"{path_to_file}/{file_name}"

        self.emailVerifier.sign_in()
        self.bulkEmailVerifier.drop_file(email_csv_file)
        self.bulkEmailVerifier.click_upload()

        result = self.bulkEmailVerifier.check_result()
        assert result["total"] == '3'
        assert result["processed"] == '3'
        assert result["found"] == '2'