import pytest
from .pages.home_page import HomePage
from .pages.search_results_page import SearchResultsPage
from .pages.item_page import ItemPage
from .pages.cart_page import CartPage


class TestEbayCart:
    @pytest.mark.ui
    def test_add_item_to_cart(self, driver):
        """
        Test adding an item to the eBay shopping cart
        """
        # Initialize page objects
        home_page = HomePage(driver)
        search_results_page = SearchResultsPage(driver)
        item_page = ItemPage(driver)
        cart_page = CartPage(driver)

        # Test steps
        home_page.navigate()
        home_page.search_item("book")
        search_results_page.click_first_result()
        item_page.add_to_cart()

        # Verification
        cart_count = cart_page.get_cart_count()
        assert cart_count == "1", f"Expected cart count to be 1, but got {cart_count}"