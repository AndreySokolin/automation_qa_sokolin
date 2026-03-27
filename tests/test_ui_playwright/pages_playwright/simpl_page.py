from playwright.sync_api import expect
from tests.test_ui_playwright.pages_playwright import locators


class SimplPage:

    def __init__(self, page):  # Объявляем "goto" и передаем "page"
        self.page = page

    def open_simpl_tab(self):
        self.page.goto("https://www.qa-practice.com/elements/button/simple")

    def check_visible_click_button(self):
        button = self.page.locator(locators.SIMPL_BUTTON_LOCATOR)
        expect(button).to_be_visible()

    def click_on_simpl_button(self):
        button = self.page.locator(locators.SIMPL_BUTTON_LOCATOR)
        button.click()

    def check_result_after_click_(self, text):
        result = self.page.locator(locators.CHECK_RESULT)
        expect(result).to_have_text(text)