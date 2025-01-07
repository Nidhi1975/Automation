from selenium.webdriver.common.by import By
from .base_page import BasePage

class SearchResultsPage(BasePage):
    FIRST_RESULT = (By.CSS_SELECTOR, "div.s-item__info a")

    def click_first_result(self):
        self.click(self.FIRST_RESULT)

# tests/ui/pages/item_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class ItemPage(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, "isCartBtn_btn")

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)