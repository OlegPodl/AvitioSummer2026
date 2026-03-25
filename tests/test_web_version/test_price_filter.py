from pages.listings_page import ListingsPage


def test_price_filter_01(driver):
    page = ListingsPage(driver)

    page.open()

    page.set_min_price("1000")
    page.set_max_price("10000")

    prices = page.get_all_prices()

    assert len(prices) > 0, "Нет объявлений после применения фильтра"

    for price in prices:
        assert 1000 <= price <= 10000, f"Цена {price} вне диапазона 1000-10000"

def test_price_filter_02(driver):
    page = ListingsPage(driver)

    page.open()

    page.set_min_price("-10000")
    page.set_max_price("-1000")

    status = page.check_is_cards_visible()
    assert not status, f"Фильтр с отрицательными значениями применен успешно"

    assert page.check_is_msg_present(), f"Кнопка сброса фильтров не доступна"

def test_price_filter_03(driver):
    page = ListingsPage(driver)
    page.open()

    page.set_min_price("abc")
    page.set_max_price("cde")

    min_val = page.get_min_price_val()
    max_val = page.get_max_price_val()

    assert len(min_val) == 0 and len(max_val) == 0, f"Фильтр с буквенными значениями заполнен успешно"

def test_price_filter_04(driver):
    page = ListingsPage(driver)
    page.open()

    page.set_min_price("@@@")
    page.set_max_price("%%%")

    min_val = page.get_min_price_val()
    max_val = page.get_max_price_val()

    assert len(min_val) == 0 and len(max_val) == 0, f"Фильтр с символьными значениями заполнен успешно"

def test_price_filter_05(driver):
    page = ListingsPage(driver)
    page.open()

    page.set_min_price("10000")
    page.set_max_price("1000")

    status = page.check_is_cards_visible()
    assert page.check_is_msg_present(), f"Кнопка сброса фильтров не доступна"
    assert not status, f"Фильтр с отрицательными значениями применен успешно"

def test_price_filter_06(driver):
    page = ListingsPage(driver)
    page.open()
    num_of_all_listings = page.count_listings()

    page.set_min_price("")
    page.set_max_price("")

    status = page.check_is_cards_visible()
    assert status, f"Список объявлений пуст"

    num_of_all_listings_after_filters = page.count_listings()

    assert num_of_all_listings == num_of_all_listings_after_filters, f'Показаны не все объявления'


    