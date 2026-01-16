from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class AdminAddUserPage:
    MENU_ADMIN = (By.XPATH, "//span[text()='Admin']")
    USER_MANAGEMENT = (By.XPATH, "//span[text()='User Management ']")
    USERS = (By.XPATH, "//a[text()='Users']")
    ADD_BUTTON = (By.XPATH, "//button[text()=' Add ']")
    USER_ROLE_DROPDOWN = (By.XPATH, "(//div[@class='oxd-select-text-input'])[1]")
    STATUS_DROPDOWN = (By.XPATH, "(//div[@class='oxd-select-text-input'])[2]")
    EMPLOYEE_NAME_BOX = (By.XPATH, "//input[@placeholder='Type for hints...']")
    USERNAME = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
    PASSWORD = (By.XPATH, "(//input[@type='password'])[1]")
    CONFIRM_PASSWORD = (By.XPATH, "(//input[@type='password'])[2]")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
    SUCCESS_TOAST = (By.XPATH, "//div[contains(@class,'toast--success')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate_to_add_user(self):
        self.wait.until(EC.element_to_be_clickable(self.MENU_ADMIN)).click()
        self.wait.until(EC.element_to_be_clickable(self.USER_MANAGEMENT)).click()
        self.wait.until(EC.element_to_be_clickable(self.USERS)).click()
        self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON)).click()

    def create_user(self, role: str, emp_name: str, username: str, password: str):
        # Role
        self.wait.until(EC.element_to_be_clickable(self.USER_ROLE_DROPDOWN)).click()
        self.driver.find_element(By.XPATH, f"//span[text()='{role}']").click()

        # Employee name (auto-suggest)
        self.driver.find_element(*self.EMPLOYEE_NAME_BOX).send_keys(emp_name)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//span[text()='{emp_name}']"))).click()

        # Status = Enabled
        self.driver.find_element(*self.STATUS_DROPDOWN).click()
        self.driver.find_element(By.XPATH, "//span[text()='Enabled']").click()

        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.CONFIRM_PASSWORD).send_keys(password)
        self.driver.find_element(*self.SAVE_BUTTON).click()
        self.wait.until(EC.visibility_of_element_located(self.SUCCESS_TOAST))
