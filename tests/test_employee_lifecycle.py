import json
import os
from pathlib import Path
import pytest
from loguru import logger
from pages.login_page import LoginPage
from pages.pim_add_employee_page import PIMAddEmployeePage
from pages.admin_add_user_page import AdminAddUserPage
from pages.dashboard_page import DashboardPage

DATA_FILE = Path(__file__).parent.parent / "data" / "employee.json"

@pytest.fixture(scope="class")
def employee_data():
    with open(DATA_FILE) as f:
        return json.load(f)

class TestEmployeeLifecycle:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.pim_page = PIMAddEmployeePage(driver)
        self.admin_page = AdminAddUserPage(driver)
        self.dashboard = DashboardPage(driver)

    def test_full_employee_lifecycle(self, employee_data):
        logger.info("Step 1: Login as admin")
        self.login_page.open()
        self.login_page.login("Admin", "admin123")
        assert self.login_page.is_dashboard_displayed(), "Admin login failed"

        logger.info("Step 2: Add new employee")
        self.pim_page.navigate_to_add_employee()
        self.pim_page.add_employee(
            employee_data["first_name"],
            employee_data["middle_name"],
            employee_data["last_name"],
            employee_data["employee_id"],
            employee_data.get("photo")
        )

        logger.info("Step 3: Create user account for the employee")
        self.admin_page.navigate_to_add_user()
        full_name = f"{employee_data['first_name']} {employee_data['last_name']}"
        self.admin_page.create_user(
            employee_data["role"],
            full_name,
            employee_data["username"],
            employee_data["password"]
        )

        logger.info("Step 4: Logout as admin")
        self.login_page.logout()

        logger.info("Step 5: Login as new employee")
        self.login_page.login(employee_data["username"], employee_data["password"])
        assert self.login_page.is_dashboard_displayed(), "New user login failed"

        welcome = self.dashboard.get_welcome_text()
        logger.info(f"Welcome text found: {welcome}")
        assert employee_data["first_name"] in welcome, "First name not found in welcome text"

        logger.info("Step 6: Logout as employee")
        self.login_page.logout()
