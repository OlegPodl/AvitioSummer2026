from selenium.webdriver.common.by import By

WAITING_TIME = 15

URL = "https://cerulean-praline-8e5aa6.netlify.app/"
MIN_PRICE_INPUT = (By.CSS_SELECTOR, 'input[placeholder = "От"]')
MAX_PRICE_INPUT = (By.CSS_SELECTOR, 'input[placeholder = "До"]')
PRICE_ELEMENTS = (By.CLASS_NAME, "_card__price_15fhn_241")
CATEGORY_ELEMENT = (By.CLASS_NAME, "_card__category_15fhn_259")
URGENT_FLAG_ELEMENTS = (By.CLASS_NAME, "_card__priority_15fhn_172")

STATISTIC_BUTTON = (By.CSS_SELECTOR, "a[href='/stats']")
LISTINGS_BUTTON = (By.CSS_SELECTOR, "a[href='/list']")
TIMER = (By.CLASS_NAME, "_timeValue_ir5wu_112")
UPDATE_BUTTON = (By.CLASS_NAME, "_refreshButton_ir5wu_16")
STOP_BUTTON = (By.CLASS_NAME, "_toggleIcon_ir5wu_94")
START_BUTTON = (By.CLASS_NAME, "_toggleButton_ir5wu_69")