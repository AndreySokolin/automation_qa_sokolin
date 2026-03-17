import time

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
import allure
import pytest



@allure.feature("Корзина")
@allure.story("Проверка функционала корзины")
class TestCart:

    @allure.title("Добавление товара в корзину")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_add_item_to_cart(self, driver):
        """Проверка добавления товара в корзину"""
        login_page = LoginPage(driver)
        login_page.open()
        inventory_page = login_page.login_as_valid_user()
        initial_count = inventory_page.get_cart_count()
        inventory_page.add_item_to_cart("Sauce Labs Backpack")
        new_count = inventory_page.get_cart_count()
        assert new_count == initial_count + 1, "Товар не добавился в корзину"

    @allure.title("Добавление нескольких товаров в корзину")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_add_multiple_items(self, driver):
        """Проверка добавления нескольких товаров"""
        login_page = LoginPage(driver)
        login_page.open()
        inventory_page = login_page.login_as_valid_user()

        items_to_add = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt"]

        for item in items_to_add:
            inventory_page.add_item_to_cart(item)

        assert inventory_page.get_cart_count() == len(items_to_add), "Не все товары добавились"

    @allure.title("Проверка сохранения товаров в корзине после выхода")
    @allure.severity(allure.severity_level.NORMAL)
    def test_cart_persistence_after_logout(self, driver):
        """Проверка, что корзина сохраняется после выхода и повторного входа"""
        login_page = LoginPage(driver)
        login_page.open()

        # Первый вход и добавление товара
        inventory_page = login_page.login_as_valid_user()
        inventory_page.add_item_to_cart("Sauce Labs Backpack")
        assert inventory_page.get_cart_count() == 1

        # Выход
        inventory_page.logout()

        # Повторный вход
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Проверка корзины
        inventory_page = InventoryPage(driver)
        assert inventory_page.get_cart_count() == 1, "Корзина не сохранилась после выхода"