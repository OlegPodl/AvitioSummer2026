import pytest
import logging
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

FAILED_LOG_FILE = "failed_tests.log"

logger = logging.getLogger("failed_logger")

# чтобы не дублировать handlers при повторном импорте
if not logger.handlers:
    file_handler = logging.FileHandler(FAILED_LOG_FILE, encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    mobile_emulation = {
        "deviceName": "iPhone X"
    }
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), 
                              options=options,
                              )
    driver.implicitly_wait(5)

    yield driver

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        logger.error("=" * 80)
        logger.error(f"TIME: {datetime.now()}")
        logger.error(f"TEST FAILED: {item.nodeid}")
        logger.error(str(report.longrepr))