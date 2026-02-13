"""
Products Page Object Model
"""
from pages.base_page import BasePage
import allure


class ProductsPage(BasePage):
    """Products page object with locators and methods"""

    # Locators
    ALL_PRODUCTS_TITLE = ".title.text-center"
    PRODUCTS_LIST = ".features_items"
    PRODUCT_ITEM = ".col-sm-4"
    ADD_TO_CART_BUTTON = ".overlay-content .add-to-cart"
    CONTINUE_SHOPPING_BUTTON = "button:has-text('Continue Shopping')"
    VIEW_CART_MODAL_LINK = "a:has-text('View Cart')"
    SEARCH_INPUT = "#search_product"
    SEARCH_BUTTON = "#submit_search"

    def __init__(self, page):
        super().__init__(page)

    @allure.step("Verify products page is loaded")
    def is_products_page_loaded(self) -> bool:
        """Check if products page is loaded"""
        return self.is_visible(self.ALL_PRODUCTS_TITLE)

    @allure.step("Get product locator by index: {index}")
    def get_product_by_index(self, index: int) -> str:
        """Get product element by index (1-based)"""
        return f"({self.PRODUCT_ITEM})[{index}]"

    @allure.step("Hover over product at index: {index}")
    def hover_on_product(self, index: int):
        """Hover over a product to reveal Add to Cart button"""
        product_locator = self.get_product_by_index(index)
        self.page.locator(product_locator).hover()

    @allure.step("Add product to cart at index: {index}")
    def add_product_to_cart(self, index: int):
        """Add a product to cart by index"""
        product_locator = self.get_product_by_index(index)
        # Hover over product
        self.page.locator(product_locator).hover()
        # Click add to cart button within the hovered product
        add_to_cart = f"{product_locator} {self.ADD_TO_CART_BUTTON}"
        self.click(add_to_cart)
        # Wait for modal to appear
        self.wait_for_element(self.CONTINUE_SHOPPING_BUTTON)
        self.take_screenshot(f"product_{index}_added")

    @allure.step("Continue shopping after adding product")
    def click_continue_shopping(self):
        """Click Continue Shopping button in modal"""
        self.click(self.CONTINUE_SHOPPING_BUTTON)

    @allure.step("View cart from modal")
    def click_view_cart_modal(self):
        """Click View Cart link in modal"""
        self.click(self.VIEW_CART_MODAL_LINK)

    @allure.step("Add multiple products to cart: {product_indices}")
    def add_multiple_products(self, product_indices: list):
        """Add multiple products to cart"""
        for index in product_indices:
            self.add_product_to_cart(index)
            if index != product_indices[-1]:  # Don't click continue shopping for the last product
                self.click_continue_shopping()