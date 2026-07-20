# 🤖 OrangeHRM Pytest Automation Framework

Automated end-to-end web testing framework built with **Python**, **Pytest**, and **Selenium WebDriver** for testing the OrangeHRM portal.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)

---

## 🌟 Key Features

- 🧪 **Page Object Model (POM)**: Decoupled UI page locators and test assertions for maintainable automation.
- 📊 **Pytest Test Runner**: Fixtures for browser initialization, teardown, and parameterized test execution.
- 📄 **HTML Test Reports**: Automated test execution logging and screenshot captures on failures.
- 🔑 **Authentication & HR Workflow Testing**: Automated validation of user logins, employee management, and leave requests.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Chrome / Firefox browser & WebDriver

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AkBePEEK/orange-hrm-pytest-automation.git
   cd orange-hrm-pytest-automation
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install pytest pytest-html selenium webdriver-manager
   ```

4. **Run the test suite:**
   ```bash
   pytest --html=report.html --self-contained-html
   ```
