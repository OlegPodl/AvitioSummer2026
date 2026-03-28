# QA Automation Project — Moderation Platform Tests

Автоматизированный набор тестов для платформы модерации объявлений.

Проект покрывает ключевые пользовательские сценарии на:
- главной странице (/list)
- странице статистики (/stats)
- мобильной версии интерфейса

---

## 📁 Структура проекта
## Задание 1 
### [**report_image_bugs.md**](\report_image_bugs.md) заметки по багам из первого задания

## Задание 2
```
pages/                 Page Object Model (POM)
  listings_page.py     логика главной страницы
  statistics_page.py   логика страницы статистики

tests/
  test_mobile/
    test_mobile.py     тесты мобильной версии (theme toggle)
  test_web_version/
    test_category_filter.py
    test_price_filter.py
    test_sort_by_price.py
    test_statistic_page.py
    test_toggle.py

conftest.py           фикстуры pytest (driver setup)
requirements.txt      зависимости проекта

TESTCASES.md         тест-кейсы
BUGS.md              найденные дефекты
```

---

## 🚀 Установка и запуск

### 1. Клонировать репозиторий
```bash
git clone <repo_url>
cd <repo_name>
```

### 2. Создать виртуальное окружение
```bash
python -m venv venv
source venv/bin/activate
venv\Scripts\activate
```

### 3. Установить зависимости
```bash
pip install -r requirements.txt
```

---

## ▶️ Запуск тестов

### Все тесты
```bash
pytest -v
```

### Web тесты
```bash
pytest tests/test_web_version/
```

### Mobile тесты
```bash
pytest tests/test_mobile/
```

---

## 🧪 Подход

- pytest + Selenium + webdriver_manager
- Page Object Model
- динамические ожидания WebDriverWait

---
