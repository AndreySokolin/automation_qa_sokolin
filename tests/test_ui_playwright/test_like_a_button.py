from tests.test_ui_playwright.pages_playwright.like_a_button_page import LikeAButtonPage
from tests.test_ui_playwright.pages_playwright import locators
from playwright.sync_api import Page


def test_looks_like_exists(page: Page): # Проверка видимости кнопки на странице 2
    like_a_button = LikeAButtonPage(page)
    like_a_button.open_like_a_button_tab() # Открыть вкладку
    like_a_button.check_visible_click_button() # Проверить наличие кнопки


def test_looks_like_click(page: Page): # Проверка клика по кнопке на странице 2
    like_a_button = LikeAButtonPage(page)
    like_a_button.open_like_a_button_tab()  # Открыть вкладку
    like_a_button.click_on_like_a_button() # Кликнуть на кнопку
    like_a_button.check_result_after_click_(locators.CHECK_TEXT_IN_RESULT) # Проверить, что клик произошел
