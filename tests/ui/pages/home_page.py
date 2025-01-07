from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    SEARCH_BOX = (By.ID, "gh-ac")
    SEARCH_BUTTON = (By.ID, "gh-btn")

    def navigate(self):
        self.driver.get("https://www.ebay.com")

    def search_item(self, item):
        self.send_keys(self.SEARCH_BOX, item)
        self.click(self.SEARCH_BUTTON)