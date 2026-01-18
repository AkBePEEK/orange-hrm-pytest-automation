# conftest.py
import os
import sys
from datetime import datetime
from pathlib import Path

import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from loguru import logger

# ------------- logging setup -------------
logger.remove()
logger.add(
    sys.stderr,
    colorize=True,
    format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{message}</cyan>",
    level="INFO",
    enqueue=True,          # ← allows late writes
)
# ------------- folders -------------
REPORT_DIR = Path("report")
REPORT_DIR.mkdir(exist_ok=True)
SHOT_DIR = Path("report/screenshots")
SHOT_DIR.mkdir(parents=True, exist_ok=True)


def take_screenshot(driver, nodeid: str) -> str:
    name = f"{nodeid.replace('::', '_')}_{datetime.now():%H%M%S}.png"
    path = str(SHOT_DIR / name)
    driver.save_screenshot(path)
    logger.error(f"Screenshot saved: {path}")
    return path



# ------------- driver fixture -------------
def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="run Chrome headless")


@pytest.fixture(scope="class")
def driver(request):
    logger.info("Starting Chrome driver")
    opt = webdriver.ChromeOptions()
    if request.config.getoption("--headless"):
        opt.add_argument("--headless=new")
    opt.add_argument("--start-maximized")

    drv = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)
    yield drv
    drv.quit()
    logger.info("Chrome driver stopped")

# ------------- screenshot on failure -------------
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed and pytest_html:
        # driver is injected into the *class* by the fixture above
        driver = getattr(item.cls, "driver", None)
        if driver:  # safety check
            path = take_screenshot(driver, item.nodeid)
            extra = getattr(rep, "extras", [])
            extra.append(pytest_html.extras.image(path))
            rep.extras = extra