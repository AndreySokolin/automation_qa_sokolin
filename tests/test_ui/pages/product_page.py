import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage


class ProductPage(BasePage):
    """Page Object для детальной страницы товара"""

    # Локаторы
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_details_name")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_details_price")
    PRODUCT_DESC = (By.CLASS_NAME, "inventory_details_desc")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn_inventory")
    BACK_TO_PRODUCTS_BUTTON = (By.ID, "back-to-products")

    @allure.step("Получить название товара")
    def get_name(self) -> str:
        """Получить название товара"""
        return self._get_text(self.PRODUCT_NAME)

    @allure.step("Получить цену товара")
    def get_price(self) -> str:
        """Получить цену товара"""
        return self._get_text(self.PRODUCT_PRICE)

    @allure.step("Получить описание товара")
    def get_description(self) -> str:
        """Получить описание товара"""
        return self._get_text(self.PRODUCT_DESC)

    @allure.step("Добавить товар в корзину")
    def add_to_cart(self):
        """Добавить текущий товар в корзину"""
        self._click(self.ADD_TO_CART_BUTTON)

    @allure.step("Проверить, что это страница товара {expected_name}")
    def is_product_page(self, expected_name: str) -> bool:
        """Проверить, что мы на странице нужного товара"""
        return self.get_name() == expected_name

    @allure.step("Вернуться к списку товаров")
    def back_to_products(self):
        """Вернуться на главную страницу с товарами"""
        self._click(self.BACK_TO_PRODUCTS_BUTTON)
        from tests.test_ui.pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)