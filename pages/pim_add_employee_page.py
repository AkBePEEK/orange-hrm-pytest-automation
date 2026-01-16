import os
from typing import Optional
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PIMAddEmployeePage:
    MENU_PIM = (By.XPATH, "//span[text()='PIM']")
    ADD_BUTTON = (By.XPATH, "//button[text()=' Add ']")
    FIRST_NAME = (By.NAME, "firstName")
    MIDDLE_NAME = (By.NAME, "middleName")
    LAST_NAME = (By.NAME, "lastName")
    EMPLOYEE_ID = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[5]")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
    PROFILE_HEADER = (By.XPATH, "//h6[contains(.,'Personal Details')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate_to_add_employee(self):
        self.wait.until(EC.element_to_be_clickable(self.MENU_PIM)).click()
        self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON)).click()

    def add_employee(self, first: str, middle: str, last: str, emp_id: str, photo_path: Optional[str] = None):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(first)
        self.driver.find_element(*self.MIDDLE_NAME).send_keys(middle)
        self.driver.find_element(*self.LAST_NAME).send_keys(last)
        # clear & set employee id
        id_box = self.driver.find_element(*self.EMPLOYEE_ID)
        id_box.clear()
        id_box.send_keys(emp_id)

        if photo_path and os.path.isfile(photo_path):
            self.driver.find_element(By.XPATH, "//input[@type='file']").send_keys(os.path.abspath(photo_path))

        self.driver.find_element(*self.SAVE_BUTTON).click()
        # wait for personal details page
        self.wait.until(EC.visibility_of_element_located(self.PROFILE_HEADER))

    def get_employee_id(self) -> str:
        return self.driver.find_element(*self.EMPLOYEE_ID).get_attribute("value")
