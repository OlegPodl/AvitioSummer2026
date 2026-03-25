from pages.listings_page import ListingsPage

def test_sorted_by_price_01(driver):
    page = ListingsPage(driver)
    page.open()

    page.set_selector_sort_by("Цене")
    page.set_selector_order("По убыванию")

    prices = page.get_all_prices()
    sort_prices = sorted(prices, reverse=True)

    assert prices == sort_prices, f"Объявления не отсортированны по цене в порядке убывания"

def test_sorted_by_price_02(driver):
    page = ListingsPage(driver)
    page.open()

    page.set_selector_sort_by("Цене")
    page.set_selector_order("По возрастанию")

    prices = page.get_all_prices()
    sort_prices = sorted(prices)

    assert prices == sort_prices, f"Объявления не отсортированны по цене в порядке возрастания"
