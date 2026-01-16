# orange-hrm-pytest-automation
End-to-end web-automation framework for OrangeHRM Demo site (https://opensource-demo.orangehrmlive.com)
Built with Python • pytest • Selenium • Loguru • pytest-html
# ✅ Features
Modular Page-Object pattern – clean separation of UI and test logic
Data-driven tests – JSON payloads for employees / users
Rich HTML reports – screenshots auto-attached on failure
Parallel-ready – pytest-xdist compatible
CI friendly – runs headless on GitHub Actions out-of-the-box

# 📁 Project tree
orange-hrm-pytest-automation/
├── pages/                      # Page-Object classes

│   ├── login_page.py

│   ├── pim_add_employee_page.py

│   ├── admin_add_user_page.py

│   └── dashboard_page.py

├── tests/

│   └── test_employee_lifecycle.py

├── utils/

│   └── screenshot_util.py

├── data/

│   └── employee.json

├── report/                     # generated after run

├── conftest.py

├── pytest.ini

├── requirements.txt

└── README.md

# 🚀 Quick start
Clone the repo

git clone https://github.com/YOUR_USERNAME/orange-hrm-pytest-automation.git
cd orange-hrm-pytest-automation

#Create & activate a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# Install dependencies

pip install -r requirements.txt

Run the full suite

pytest
# Headless (CI) mode:

pytest --headless

Open the report
open report/report.html

# 📊 Sample Report
./docs/report-preview.png

🔧 Customisation
Table
| Item              | Where                | Example                                 |
| ----------------- | -------------------- | --------------------------------------- |
| New employee data | `data/employee.json` | add more JSON files                     |
| Browser           | `conftest.py`        | switch to Firefox/Edge                  |
| Wait timeouts     | each page class      | change `WebDriverWait(driver, 10)`      |
| Log level         | `conftest.py`        | `logger.add(sys.stderr, level="DEBUG")` |

# 🧪 Run single test

pytest -k valid_login
pytest tests/test_employee_lifecycle.py::TestEmployeeLifecycle::test_full_employee_lifecycle -v

# 🚶‍♂️ Headless CI (GitHub Actions)
Already provided: .github/workflows/run-tests.yml
Push to main – tests execute on Ubuntu + Chrome headless and artifacts (report + screenshots) are uploaded.

# 🐍 Python version
3.8+ (tested on 3.8 – 3.12)

# 🤝 Contributing
Pull-requests welcome!
Please run black + flake8 before submitting.
