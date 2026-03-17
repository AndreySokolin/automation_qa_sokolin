import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


@pytest.fixture(scope="function")
def driver():
    """Фикстура с отключенными уведомлениями о паролях и поддержкой CI/CD"""

    # Настройка опций браузера
    options = Options()

    # === ВАЖНО ДЛЯ CI/CD ===
    # Проверяем, запущены ли тесты в GitHub Actions
    if os.getenv('CI') == 'true':
        options.add_argument("--headless")  # Безголовый режим
        options.add_argument("--no-sandbox")  # Обязательно для Linux
        options.add_argument("--disable-dev-shm-usage")  # Для избежания проблем с памятью
        options.add_argument("--disable-gpu")  # Для Windows (но оставь)
        options.add_argument("--remote-debugging-port=9222")  # Для отладки

    # Базовые настройки (работают везде)
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    # Отключаем всё, связанное с паролями
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "profile.password_manager_auto_signin": False,
        "profile.default_content_setting_values.notifications": 2,
    })

    # Отключаем пузырь сохранения паролей
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-password-generation")

    # Дополнительные настройки для стабильности в CI
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-web-security")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-running-insecure-content")

    # Используем Selenium Manager для автоматической загрузки драйвера
    driver = webdriver.Chrome(options=options)

    # Открываем сайт
    driver.get("https://www.saucedemo.com/")

    yield driver
    driver.quit()