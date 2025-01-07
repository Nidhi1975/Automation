from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    CART_COUNT = (By.CLASS_NAME, "cart-count")

    def get_cart_count(self):
        return self.get_text(self.CART_COUNT)