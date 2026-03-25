import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

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