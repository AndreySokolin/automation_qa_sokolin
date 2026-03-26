import allure
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@allure.feature("Авторизация")
@allure.story("Проверка функционала входа в систему")
class TestLogin:

    @allure.title("Успешный вход с валидными учетными данными")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    def test_valid_login(self, driver):
        """Проверка входа с корректными учетными данными"""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        assert inventory_page.is_on_page(), "Не удалось войти в систему"
        assert inventory_page.get_items_count() > 0, "Товары не отображаются"

    @allure.title("Проверка входа с заблокированным пользователем")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_locked_out_user(self, driver):
        """Проверка входа с заблокированным пользователем"""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("locked_out_user", "secret_sauce")

        assert login_page.is_error_displayed(), "Сообщение об ошибке не отображается"
        error_text = login_page.get_error_message()
        assert "locked out" in error_text.lower(), f"Неверный текст ошибки: {error_text}"

    @allure.title("Параметризованная проверка различных пользователей")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("username,password,should_succeed", [
        ("standard_user", "secret_sauce", True),
        ("problem_user", "secret_sauce", True),
        ("performance_glitch_user", "secret_sauce", True),
        ("invalid_user", "wrong_pass", False),
        ("", "", False),
    ])
    def test_multiple_users(self, driver, username, password, should_succeed):
        """Параметризованная проверка входа с разными пользователями"""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(username, password)

        if should_succeed:
            inventory_page = InventoryPage(driver)
            assert inventory_page.is_on_page(), f"Вход не удался для {username}"
        else:
            assert login_page.is_error_displayed(), f"Ожидалась ошибка для {username}"

    @allure.title("Проверка полей ввода после ошибки")
    @allure.severity(allure.severity_level.MINOR)
    def test_fields_after_error(self, driver):
        """Проверка, что поля очищаются после ввода неверных данных"""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("wrong", "wrong")

        assert login_page.is_error_displayed()
        login_page.clear_fields()

        # Повторный ввод с корректными данными
        login_page.login("standard_user", "secret_sauce")
        inventory_page = InventoryPage(driver)
        assert inventory_page.is_on_page()