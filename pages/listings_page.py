from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

class ListingsPage:

    URL = "https://cerulean-praline-8e5aa6.netlify.app/"

    MIN_PRICE_INPUT = (By.CSS_SELECTOR, 'input[placeholder = "От"]')
    MAX_PRICE_INPUT = (By.CSS_SELECTOR, 'input[placeholder = "До"]')

    PRICE_ELEMENTS = (By.CLASS_NAME, "_card__price_15fhn_241")
    CATEGORY_ELEMENT = (By.CLASS_NAME, "_card__category_15fhn_259")
    URGENT_FLAG_ELEMENTS = (By.CLASS_NAME, "_card__priority_15fhn_172")
    STATISTIC_BUTTON = (By.CSS_SELECTOR, "a[href='/stats']")
    LISTINGS_BUTTON = (By.CSS_SELECTOR, "a[href='/list']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def set_min_price(self, value):
        element = self.wait.until(EC.visibility_of_element_located(self.MIN_PRICE_INPUT))
        element.clear()
        element.send_keys(value)

    def set_max_price(self, value):
        element = self.wait.until(EC.visibility_of_element_located(self.MAX_PRICE_INPUT))
        element.clear()
        element.send_keys(value)

    def get_all_prices(self):
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, '_pagination__pages_a1c3m_112')))
        last_page_btn = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div._pagination__pages_a1c3m_112 button:last-of-type')
        ))
        total_pages = int(last_page_btn.text)

        prices = []
        current_page = 1

        while current_page <= total_pages:

            price_elements = self.wait.until(EC.visibility_of_all_elements_located(self.PRICE_ELEMENTS))
            for el in price_elements:
                price_text = el.text.replace(" ", "").replace("₽", "")
                if price_text.isdigit():
                    prices.append(int(price_text))

            if current_page == total_pages:
                break

            next_button = self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'button._pagination__button_a1c3m_18[aria-label="Следующая страница"]')
            ))
            next_button.click()
            self.wait.until(EC.staleness_of(price_elements[0]))
            current_page += 1

        return prices

    def check_is_cards_visible(self):
        try:
            cards = self.wait.until(EC.visibility_of_any_elements_located((By.CLASS_NAME, "_card__info_15fhn_226")))
        except TimeoutException:
            return False
        return True
    
    def check_is_msg_present(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Сбросить фильтры')]")))
            return True
        except TimeoutException:
            return False
        
    def get_min_price_val(self):
        element = self.wait.until(EC.visibility_of_element_located(self.MIN_PRICE_INPUT))
        return element.get_attribute("value")

    def get_max_price_val(self):
        element = self.wait.until(EC.visibility_of_element_located(self.MAX_PRICE_INPUT))
        return element.get_attribute("value")
    
    def count_listings(self):
        num = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "_pagination__info_a1c3m_93")))
        num = num.text.split(' ')[3]
        return int(num)
    
    def set_selector_sort_by(self, value):
        element = Select(self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//select[contains(@class, '_filters__select_')])[1]"))))
        element.select_by_visible_text(value)

    def set_selector_order(self, value):
        element = Select(self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//select[contains(@class, '_filters__select_')])[2]"))))
        element.select_by_visible_text(value)

    def set_selector_category(self, value):
        element = Select(self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//select[contains(@class, '_filters__select_')])[3]"))))
        element.select_by_visible_text(value)

    def get_all_category(self):
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, '_pagination__pages_a1c3m_112')))
        last_page_btn = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div._pagination__pages_a1c3m_112 button:last-of-type')
        ))
        total_pages = int(last_page_btn.text)

        categories = []
        current_page = 1

        while current_page <= total_pages:

            category_elements = self.wait.until(EC.visibility_of_all_elements_located(self.CATEGORY_ELEMENT))
            for el in category_elements:
                category_text = el.text.replace(" ", "")
                categories.append(category_text)

            if current_page == total_pages:
                break

            next_button = self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'button._pagination__button_a1c3m_18[aria-label="Следующая страница"]')
            ))
            next_button.click()
            if len(category_elements) > 0:
                self.wait.until(EC.staleness_of(category_elements[0]))
            current_page += 1

        return categories
    
    def count_urgent(self):
        self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, '_pagination__pages_a1c3m_112'))
        )

        last_page_btn = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div._pagination__pages_a1c3m_112 button:last-of-type')
            )
        )
        total_pages = int(last_page_btn.text)

        urgent_count = 0
        current_page = 1

        while current_page <= total_pages:
            urgent_elements = self.wait.until(
                EC.presence_of_all_elements_located(self.URGENT_FLAG_ELEMENTS)
            )

            urgent_count += len(urgent_elements)

            if current_page == total_pages:
                break

            next_button = self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'button._pagination__button_a1c3m_18[aria-label="Следующая страница"]')
                )
            )

            next_button.click()

            if urgent_elements:
                self.wait.until(EC.staleness_of(urgent_elements[0]))

            current_page += 1

        return urgent_count
    
    def set_toggle(self):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Только срочные')]")))
        element.click()

    def get_priorety_value(self):
        element = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "(//select[contains(@class, '_filters__select_')])[4]")
            )
        )
        return element.get_attribute("value")

    def get_theme(self):
        element = self.driver.find_element(By.TAG_NAME, "html")
        theme = element.get_attribute("data_theme")
        return theme
    
    def change_theme(self):
        element = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "_themeToggle_127us_1")))
        element.click()

    def go_to_statistic_page(self):
        element = self.wait.until(EC.element_to_be_clickable(self.STATISTIC_BUTTON))
        element.click()

    def go_to_listings_page(self):
        element = self.wait.until(EC.element_to_be_clickable(self.LISTINGS_BUTTON))
        element.click()