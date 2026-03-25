from pages.listings_page import ListingsPage
from pages.statistics_page import StatisticPage

def test_mobile_version_01(driver):
    page = ListingsPage(driver)
    page.open()

    theme = page.get_theme()
    page.go_to_statistic_page()
    theme2 = page.get_theme()
    assert theme == theme2, f"Тема сменяется не пользователем при переходе от объявлений к статистике тема объявлений: {theme}, тема статистики: {theme2}"
    page.go_to_listings_page()
    theme = page.get_theme()
    assert theme == theme2, f"Тема сменяется не пользователем при переходе от статистики к объявлениям тема объявлений: {theme}, тема статистики: {theme2}"

    page.change_theme()

    theme = page.get_theme()
    page.go_to_statistic_page()
    theme2 = page.get_theme()
    assert theme == theme2, f"Тема сменяется не пользователем при переходе от объявлений к статистике тема объявлений: {theme}, тема статистики: {theme2}"
    page.go_to_listings_page()
    theme = page.get_theme()
    assert theme == theme2, f"Тема сменяется не пользователем при переходе от объявлений к статистике тема объявлений: {theme}, тема статистики: {theme2}"
