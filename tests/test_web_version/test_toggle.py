from pages.listings_page import ListingsPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_toggle_express_01(driver):
    page = ListingsPage(driver)
    page.open()

    toggle = page.wait.until(EC.presence_of_element_located((By.CLASS_NAME, '_urgentToggle__input_h1vv9_14')))
    status = toggle.is_enabled()
    if not status:
        page.set_toggle()
    
    all_listings = page.count_listings()
    listings_with_flag = page.count_urgent()

    assert page.get_priorety_value() == '', f"Приоритет в фильтре не совпадает с тогглом {page.get_priorety_value()}"
    assert all_listings == listings_with_flag, f"Не все объявления помечены флагом, объявлений без флага: {all_listings - listings_with_flag}"

def test_toggle_express_02(driver):
    page = ListingsPage(driver)
    page.open()

    all_listings = page.count_listings()

    toggle = page.wait.until(EC.presence_of_element_located((By.CLASS_NAME, '_urgentToggle__input_h1vv9_14')))
    status = toggle.is_enabled()
    if status:
        page.set_toggle()
    
    listings_without_flag = page.count_listings()

    assert page.get_priorety_value() == 'urgent', f"Приоритет в фильтре не совпадает с тогглом {page.get_priorety_value()}"
    assert all_listings == listings_without_flag, f"Показаны не все объявления"
