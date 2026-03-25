import pytest
from pages.listings_page import ListingsPage

CATEGORIES = ['Электроника', 'Недвижимость', "Транспорт", "Работа", "Услуги", "Животные", "Мода", "Детское"]

def test_category_01(driver):
    page = ListingsPage(driver)
    page.open()

    all_listings = page.count_listings()

    page.set_selector_category("Все категории")
    page.check_is_cards_visible()

    all_category_listings = page.count_listings()

    assert all_listings == all_category_listings, f"Не все объявления в категории 'Все категории'"

@pytest.mark.parametrize("category", CATEGORIES)
def test_category_filter(driver, category):
    page = ListingsPage(driver)
    page.open()

    page.set_selector_category(category)  # обратите внимание на опечатку "catogory" -> "category"
    page.check_is_cards_visible()

    cats = set(page.get_all_category())

    assert len(cats) == 1, f'При выборе категории {category}, показаны объявления и других категорий: {cats}'
    assert category in cats, f"При выборе категории {category} показаны объявления категорий {cats}"