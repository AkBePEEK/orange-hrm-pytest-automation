from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    WELCOME_NAME = (By.CLASS_NAME, "oxd-userdropdown-name")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_welcome_text(self) -> str:
        return self.wait.until(EC.visibility_of_element_located(self.WELCOME_NAME)).text
