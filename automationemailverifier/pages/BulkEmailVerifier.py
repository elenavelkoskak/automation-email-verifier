from selenium.webdriver.common.by import By

from automationemailverifier.pages.BasePage import BasePage

class BulkEmailVerifier(BasePage):
    DROP_FILE = (By.ID, "file")
    UPLOAD_FILE = (By.ID, "btnUploadDocument")

    def drop_file(self, email_file):
        drop_file = self.driver.find_element(*self.DROP_FILE)
        drop_file.send_keys(email_file)

    def click_upload(self):
        upload_file = self.driver.find_element(*self.UPLOAD_FILE)
        upload_file.click()

    def check_result(self):
        elem = self.driver.find_element(By.CSS_SELECTOR, "#contactBulkWrap > div > div:nth-child(1) > div > div > h3")

        total_value = elem.find_element(By.XPATH, "./../div[@class='row']/div[1]/h3").text
        processed_value = elem.find_element(By.XPATH, "./../div[@class='row']/div[2]/h3").text
        found_value = elem.find_element(By.XPATH, "./../div[@class='row']/div[3]/h3").text

        return {
            "total": total_value,
            "processed": processed_value,
            "found": found_value
        }
