# Проект автоматизации тестирования интернет-магазина SauceDemo

## Описание
Учебный проект по автоматизации тестирования сайта [SauceDemo](). Реализованы UI и API тесты с использованием современных инструментов и подходов.

## Технологии
- Python 3.11
- Pytest - тестовый фреймворк
- Selenium WebDriver - UI тесты
- Requests - API тесты
- Allure - отчетность
- Page Object Model - паттерн проектирования

## Структура проекта

my_awesome_test_project/
├── pages/                 # Папка для Page Objects
│   ├── __init__.py
│   ├── base_page.py       # Базовый класс для всех страниц (driver, общие методы)
│   ├── login_page.py      # Методы для страницы логина
│   └── inventory_page.py  # Методы для страницы с товарами
├── tests/                 # Папка с тестами
│   ├── __init__.py
│   ├── conftest.py        # Фикстуры Pytest (например, инициализация и закрытие браузера)
│   ├── test_login.py      # Тесты на логин
│   └── test_cart.py       # Тесты на добавление в корзину
├── utils/                 # Вспомогательные утилиты
│   ├── __init__.py
│   └── data_generator.py  # Генерация тестовых данных (имена, email)
├── reports/               # Сюда Allure будет генерировать отчеты (в .gitignore)
├── screenshots/           # Папка для скриншотов падающих тестов (в .gitignore)
├── requirements.txt       # Зависимости проекта
├── pytest.ini             # Конфигурация Pytest
└── README.md              # Описание проекта