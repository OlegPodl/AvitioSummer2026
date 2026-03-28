from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json
from urllib.parse import urlparse, parse_qs
from pages import constants

class StatisticPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, constants.WAITING_TIME)

    def open(self):
        self.driver.get(constants.URL)
        stats_button = self.wait.until(EC.element_to_be_clickable(constants.STATISTIC_BUTTON))
        stats_button.click()

    def go_to_listings_page(self):
        element = self.wait.until(EC.element_to_be_clickable(constants.LISTINGS_BUTTON))
        element.click()

    def get_time_to_update(self):
        element = self.wait.until(EC.visibility_of_element_located(constants.TIMER))
        time = element.text.split(':')
        return int(time[0])*60 + int(time[1])

    def was_update_request_sent(self, page=None, limit=None):
        logs = self.driver.get_log("performance")

        for entry in logs:
            message = json.loads(entry["message"])["message"]

            if message["method"] != "Network.requestWillBeSent":
                continue

            request = message["params"]["request"]
            url = request["url"]

            if "/api/v1/ads" not in url:
                continue

            parsed = urlparse(url)
            query = parse_qs(parsed.query)

            if page and query.get("page", [None])[0] != str(page):
                continue

            if limit and query.get("limit", [None])[0] != str(limit):
                continue

            return True

        return False
    
    def man_update(self):
        element = self.wait.until(EC.element_to_be_clickable(constants.UPDATE_BUTTON))
        element.click()

    def stop_timer(self):
        element = self.wait.until(EC.element_to_be_clickable(constants.STOP_BUTTON))
        element.click()

    def start_timer(self):
        element = self.wait.until(EC.element_to_be_clickable(constants.START_BUTTON))
        element.click()

    def is_timer_visible(self):
        try:
            element = self.wait.until(EC.visibility_of_element_located(constants.TIMER))
        except:
            return False
        return True