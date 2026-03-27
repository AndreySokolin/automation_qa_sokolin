import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .inventory_page import InventoryPage


class LoginPage(BasePage):
    """Page Object для страницы логина"""

    # Локаторы элементов
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    LOGIN_LOGO = (By.CLASS_NAME, "login_logo")

    @allure.step("Открыть страницу логина")
    def open(self):
        """Открытие страницы логина"""
        self.driver.get("https://www.saucedemo.com/")
        self._wait_for_page_load()
        assert self._is_element_present(self.LOGIN_LOGO), "Страница логина не загрузилась"

    @allure.step("Войти в систему с логином {username}")
    def login(self, username: str, password: str):
        """Выполнение входа в систему"""
        self._send_keys(self.USERNAME_INPUT, username)
        self._send_keys(self.PASSWORD_INPUT, password)
        self._click(self.LOGIN_BUTTON)

    @allure.step("Успешный вход в систему")
    def login_as_valid_user(self) -> InventoryPage:
        """Вход с валидными учетными данными и возврат страницы товаров"""
        self.login("standard_user", "secret_sauce")
        return InventoryPage(self.driver)

    @allure.step("Получить сообщение об ошибке")
    def get_error_message(self) -> str:
        """Получение текста сообщения об ошибке"""
        return self._get_text(self.ERROR_MESSAGE)

    @allure.step("Проверить наличие сообщения об ошибке")
    def is_error_displayed(self) -> bool:
        """Проверка отображения сообщения об ошибке"""
        return self._is_element_present(self.ERROR_MESSAGE)

    @allure.step("Очистить поля ввода")
    def clear_fields(self):
        """Очистка полей ввода"""
        self._send_keys(self.USERNAME_INPUT, "")
        self._send_keys(self.PASSWORD_INPUT, "")