"""
Cart Page Object Model
"""
from pages.base_page import BasePage
import allure


class CartPage(BasePage):
    """Cart page object with locators and methods"""

    # Locators
    CART_INFO_TABLE = "#cart_info_table"
    CART_ITEMS = "tr.cart_menu ~ tr"
    PRODUCT_NAME = ".cart_description h4 a"
    PRODUCT_PRICE = ".cart_price p"
    PRODUCT_QUANTITY = ".cart_quantity button"
    PRODUCT_TOTAL = ".cart_total p"
    PROCEED_TO_CHECKOUT_BUTTON = ".btn-default.check_out"
    REGISTER_LOGIN_LINK = "a[href='/login']"
    DELETE_PRODUCT_BUTTON = ".cart_quantity_delete"
    CART_EMPTY_TEXT = "#empty_cart"

    def __init__(self, page):
        super().__init__(page)

    @allure.step("Get number of items in cart")
    def get_cart_items_count(self) -> int:
        """Get the number of items in cart"""
        return self.page.locator(self.CART_ITEMS).count()

    @allure.step("Get product name at index: {index}")
    def get_product_name(self, index: int) -> str:
        """Get product name by index (0-based)"""
        products = self.page.locator(self.PRODUCT_NAME)
        return products.nth(index).inner_text()

    @allure.step("Get product price at index: {index}")
    def get_product_price(self, index: int) -> str:
        """Get product price by index (0-based)"""
        prices = self.page.locator(self.PRODUCT_PRICE)
        return prices.nth(index).inner_text()

    @allure.step("Get product quantity at index: {index}")
    def get_product_quantity(self, index: int) -> str:
        """Get product quantity by index (0-based)"""
        quantities = self.page.locator(self.PRODUCT_QUANTITY)
        return quantities.nth(index).inner_text()

    @allure.step("Get product total at index: {index}")
    def get_product_total(self, index: int) -> str:
        """Get product total price by index (0-based)"""
        totals = self.page.locator(self.PRODUCT_TOTAL)
        return totals.nth(index).inner_text()

    @allure.step("Verify cart contains {expected_count} products")
    def verify_cart_items_count(self, expected_count: int) -> bool:
        """Verify the number of items in cart"""
        actual_count = self.get_cart_items_count()
        return actual_count == expected_count

    @allure.step("Get all products in cart")
    def get_all_products_info(self) -> list:
        """Get information about all products in cart"""
        count = self.get_cart_items_count()
        products = []

        for i in range(count):
            product_info = {
                'name': self.get_product_name(i),
                'price': self.get_product_price(i),
                'quantity': self.get_product_quantity(i),
                'total': self.get_product_total(i)
            }
            products.append(product_info)

        return products

    @allure.step("Click Proceed to Checkout")
    def click_proceed_to_checkout(self):
        """Click on Proceed to Checkout button"""
        self.click(self.PROCEED_TO_CHECKOUT_BUTTON)

    @allure.step("Take cart screenshot")
    def capture_cart_state(self):
        """Take screenshot of cart"""
        self.take_screenshot("cart_state")

    @allure.step("Verify cart is not empty")
    def is_cart_not_empty(self) -> bool:
        """Check if cart has items"""
        return self.get_cart_items_count() > 0