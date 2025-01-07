from selenium.webdriver.common.by import By
from .base_page import BasePage

class ItemPage(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, "isCartBtn_btn")

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)