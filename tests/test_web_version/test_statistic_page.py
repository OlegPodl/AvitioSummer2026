from pages.statistics_page import StatisticPage
from selenium.webdriver.support.ui import WebDriverWait

def test_timer_control_container_01(driver):
    page = StatisticPage(driver)
    page.open()

    timeout = page.get_time_to_update()

    page.driver.get_log("performance")

    found = WebDriverWait(driver, timeout + 2).until(
        lambda d: page.was_update_request_sent()
    )

    assert found, f"Обновлений статистики не произошло после окончания таймера"

def test_time_control_container_02(driver):
    page = StatisticPage(driver)
    page.open()

    page.driver.get_log("performance")
    page.man_update()

    assert page.was_update_request_sent(), f"Обновление статистики не произошло после ручного обновления"

def test_time_control_container_03(driver):
    page = StatisticPage(driver)
    page.open()

    page.stop_timer()
    try:
        WebDriverWait(driver, 5).until(lambda d: False)
    except:
        pass

    assert not page.is_timer_visible(), f" Таймер продолжает отсчет после остановки таймера"

def test_time_control_container_04(driver):
    page = StatisticPage(driver)
    page.open()

    page.stop_timer()
    try:
        WebDriverWait(driver, 5).until(lambda d: False)
    except:
        pass

    assert not page.is_timer_visible(), f" Таймер продолжает отсчет после остановки таймера"

    page.start_timer()
    try:
        WebDriverWait(driver, 10).until(lambda d: False)
    except:
        pass

    assert not page.is_timer_visible(), f"Таймер не продолжил отсчет после возобновления"

    page.driver.get_log("performance")
    time2 = page.get_time_to_update()

    found = WebDriverWait(driver, time2 + 2).until(
        lambda d: page.was_update_request_sent()
    )
    assert found, f"После окончания таймера страница не была обновлена"
