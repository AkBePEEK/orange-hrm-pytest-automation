from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://opensource-demo.orangehrmlive.com/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def login(self, username: str, password: str):
        self.wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    def is_dashboard_displayed(self) -> bool:
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
        ).is_displayed()

    def logout(self):
        self.driver.find_element(By.CLASS_NAME, "oxd-userdropdown-tab").click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']"))).click()
