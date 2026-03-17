import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    """Фикстура с отключенными уведомлениями о паролях"""

    # Настройка опций браузера
    options = Options()

    # Базовые настройки
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    # === ВАЖНО: Отключаем всё, связанное с паролями ===
    options.add_experimental_option("prefs", {
        # Отключаем предложение сохранять пароли
        "credentials_enable_service": False,
        # Отключаем менеджер паролей
        "profile.password_manager_enabled": False,
        # Отключаем проверку утечек паролей (самое главное!)
        "profile.password_manager_leak_detection": False,
        # Отключаем автоматический вход
        "profile.password_manager_auto_signin": False,
        # Отключаем сохранение паролей в целом
        "profile.default_content_setting_values.notifications": 2,
        "profile.content_settings.exceptions.automatic_downloads": {},
        "profile.content_settings.exceptions.popups": {}
    })

    # Добавляем аргументы командной строки
    options.add_argument("--disable-save-password-bubble")  # Отключаем пузырь сохранения
    options.add_argument("--disable-password-generation")  # Отключаем генерацию паролей

    # Используем Selenium Manager для автоматической загрузки драйвера
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")

    yield driver
    driver.quit()