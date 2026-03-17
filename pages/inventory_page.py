from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure


class InventoryPage(BasePage):
    # Добавьте новые локаторы
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    INVENTORY_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    INVENTORY_ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    INVENTORY_ITEM_IMAGES = (By.CSS_SELECTOR, "img.inventory_item_img")

    @allure.step("Получить все товары на странице")
    def get_all_items(self) -> list:
        """Получить список всех товаров на странице"""
        item_elements = self.driver.find_elements(*self.INVENTORY_ITEMS)
        items = []
        for element in item_elements:
            items.append(InventoryItem(self.driver, element))
        return items

    @allure.step("Кликнуть по товару {item_name}")
    def click_on_product(self, item_name: str):
        """Кликнуть по названию товара для перехода в детальную карточку"""
        # Используем XPath для поиска товара по имени
        item_locator = (By.XPATH, f"//div[@class='inventory_item_name' and text()='{item_name}']")
        self._click(item_locator)

        # После клика создаем экземпляр страницы товара
        from pages.product_page import ProductPage
        return ProductPage(self.driver)

    @allure.step("Получить названия всех товаров")
    def get_all_item_names(self) -> list:
        """Получить список названий всех товаров"""
        name_elements = self.driver.find_elements(*self.INVENTORY_ITEM_NAMES)
        return [element.text for element in name_elements]

    @allure.step("Получить цены всех товаров")
    def get_all_item_prices(self) -> list:
        """Получить список цен всех товаров в числовом формате"""
        price_elements = self.driver.find_elements(*self.INVENTORY_ITEM_PRICES)
        prices = []
        for element in price_elements:
            # Преобразуем "$29.99" в 29.99
            price_text = element.text.replace('$', '')
            prices.append(float(price_text))
        return prices

    @allure.step("Найти товар по имени")
    def find_item_by_name(self, item_name: str) -> InventoryItem:
        """Найти конкретный товар по имени"""
        items = self.get_all_items()
        for item in items:
            if item.get_name() == item_name:
                return item
        raise AssertionError(f"Товар с именем '{item_name}' не найден")

# Добавьте этот класс в inventory_page.py перед классом InventoryPage
class InventoryItem:
    """Класс для работы с отдельным товаром на странице"""

    def __init__(self, driver, element):
        self.driver = driver
        self.element = element

    def get_name(self) -> str:
        """Получить название товара"""
        return self.element.find_element(By.CLASS_NAME, "inventory_item_name").text

    def get_price(self) -> str:
        """Получить цену товара"""
        return self.element.find_element(By.CLASS_NAME, "inventory_item_price").text

    def get_description(self) -> str:
        """Получить описание товара"""
        return self.element.find_element(By.CLASS_NAME, "inventory_item_desc").text

    def image_loaded(self) -> bool:
        """Проверить, загрузилось ли изображение"""
        img = self.element.find_element(By.CSS_SELECTOR, "img.inventory_item_img")
        # Проверяем, что изображение действительно загружено
        return self.driver.execute_script(
            "return arguments[0].complete && arguments[0].naturalHeight > 0",
            img
        )

    def add_to_cart(self):
        """Добавить товар в корзину"""
        button = self.element.find_element(By.CSS_SELECTOR, ".btn_inventory")
        button.click()

    def click_on_name(self):
        """Кликнуть по названию товара для перехода в детальную карточку"""
        name_link = self.element.find_element(By.CLASS_NAME, "inventory_item_name")
        name_link.click()
        from pages.product_page import ProductPage  # Импортируем здесь, чтобы избежать циклических импортов
        return ProductPage(self.driver)

class InventoryPage(BasePage):
    """Page Object для страницы с товарами"""

    # Локаторы
    PAGE_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    # Динамические локаторы (с подстановкой)
    ADD_TO_CART_BUTTON = (By.XPATH, "//div[text()='{}']/ancestor::div[@class='inventory_item']//button")
    ITEM_PRICE = (By.XPATH, "//div[text()='{}']/ancestor::div[@class='inventory_item']//div[@class='inventory_item_price']")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    @allure.step("Проверить нахождение на странице товаров")
    def is_on_page(self) -> bool:
        """Проверка, что мы на странице товаров"""
        return self._is_element_present(self.PAGE_TITLE) and "Products" in self._get_text(self.PAGE_TITLE)

    @allure.step("Получить количество товаров на странице")
    def get_items_count(self) -> int:
        """Получение количества отображаемых товаров"""
        items = self.driver.find_elements(*self.INVENTORY_ITEMS)
        return len(items)

    @allure.step("Добавить товар '{item_name}' в корзину")
    def add_item_to_cart(self, item_name: str):
        """Добавление конкретного товара в корзину"""
        locator = (self.ADD_TO_CART_BUTTON[0], self.ADD_TO_CART_BUTTON[1].format(item_name))
        self._click(locator)

    @allure.step("Получить цену товара '{item_name}'")
    def get_item_price(self, item_name: str) -> str:
        """Получение цены товара"""
        locator = (self.ITEM_PRICE[0], self.ITEM_PRICE[1].format(item_name))
        return self._get_text(locator)

    @allure.step("Получить количество товаров в корзине")
    def get_cart_count(self) -> int:
        """Получение количества товаров в корзине"""
        if self._is_element_present(self.CART_BADGE):
            return int(self._get_text(self.CART_BADGE))
        return 0

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        """Переход в корзину"""
        self._click(self.CART_LINK)

    @allure.step("Отсортировать товары по {sort_option}")
    def sort_items(self, sort_option: str):
        """Сортировка товаров"""
        from selenium.webdriver.support.ui import Select
        select = Select(self._find_element(self.SORT_DROPDOWN))
        select.select_by_visible_text(sort_option)

    @allure.step("Выйти из системы")
    def logout(self):
        """Выход из системы через бургер-меню"""
        self._click(self.BURGER_MENU)
        self._click(self.LOGOUT_BUTTON)