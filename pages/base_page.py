import logging
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from datetime import datetime
import os


class BasePage:
    """Базовый класс для всех Page Objects"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = logging.getLogger(__name__)

    def _find_element(self, locator: tuple) -> WebElement:
        """Поиск элемента с ожиданием видимости"""
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )
            self.logger.info(f"Элемент найден: {locator}")
            return element
        except TimeoutException:
            self.logger.error(f"Элемент не найден: {locator}")
            self._take_screenshot("element_not_found")
            raise

    def _click(self, locator: tuple):
        """Клик по элементу с ожиданием кликабельности"""
        try:
            element = self.wait.until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
            self.logger.info(f"Клик по элементу: {locator}")
        except Exception as e:
            self.logger.error(f"Ошибка клика: {locator}, {str(e)}")
            self._take_screenshot("click_error")
            raise

    def _send_keys(self, locator: tuple, text: str):
        """Ввод текста в поле"""
        try:
            element = self._find_element(locator)
            element.clear()
            element.send_keys(text)
            self.logger.info(f"Введен текст '{text}' в элемент: {locator}")
        except Exception as e:
            self.logger.error(f"Ошибка ввода текста: {locator}, {str(e)}")
            self._take_screenshot("send_keys_error")
            raise

    def _get_text(self, locator: tuple) -> str:
        """Получение текста элемента"""
        try:
            text = self._find_element(locator).text
            self.logger.info(f"Получен текст '{text}' из элемента: {locator}")
            return text
        except Exception as e:
            self.logger.error(f"Ошибка получения текста: {locator}, {str(e)}")
            raise

    def _is_element_present(self, locator: tuple) -> bool:
        """Проверка наличия элемента на странице"""
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def _take_screenshot(self, name: str = "screenshot"):
        """Создание скриншота"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"{name}_{timestamp}.png"
        screenshot_path = os.path.join("screenshots", screenshot_name)

        # Создаем папку screenshots, если её нет
        os.makedirs("screenshots", exist_ok=True)

        self.driver.save_screenshot(screenshot_path)
        self.logger.info(f"Скриншот сохранен: {screenshot_path}")

        # Прикрепляем скриншот к Allure отчету
        allure.attach.file(
            screenshot_path,
            name=screenshot_name,
            attachment_type=allure.attachment_type.PNG
        )

        return screenshot_path

    def _wait_for_page_load(self):
        """Ожидание загрузки страницы"""
        self.wait.until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
        self.logger.info("Страница загружена полностью")