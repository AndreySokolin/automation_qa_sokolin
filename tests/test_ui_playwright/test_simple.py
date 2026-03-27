from tests.test_ui_playwright.pages_playwright.simpl_page import SimplPage
from tests.test_ui_playwright.pages_playwright import locators
from playwright.sync_api import Page


def test_simpl_exists(page: Page): # Проверка видимости кнопки на странице 1
    simpl_page = SimplPage(page)
    simpl_page.open_simpl_tab() # Открыть вкладку
    simpl_page.check_visible_click_button() # Проверить наличие кнопки

def test_simpl_click(page: Page): # Проверить клик по кнопке на странице 1
    simpl_page = SimplPage(page)
    simpl_page.open_simpl_tab()  # Открыть вкладку
    simpl_page.click_on_simpl_button() # Кликнуть на кнопку
    simpl_page.check_result_after_click_(locators.CHECK_TEXT_IN_RESULT) # Проверить, что клик произошел
