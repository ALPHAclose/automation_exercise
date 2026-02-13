"""
Checkout Page Object Model
"""
from pages.base_page import BasePage
import allure


class CheckoutPage(BasePage):
    """Checkout page object with locators and methods"""

    # Locators
    ADDRESS_DELIVERY = ".address_delivery"
    ADDRESS_INVOICE = ".address_invoice"
    ORDER_REVIEW = "#cart_info"
    COMMENT_TEXTAREA = "textarea[name='message']"
    PLACE_ORDER_BUTTON = "a[href='/payment']"

    # Payment Page
    NAME_ON_CARD_INPUT = "input[name='name_on_card']"
    CARD_NUMBER_INPUT = "input[name='card_number']"
    CVC_INPUT = "input[name='cvc']"
    EXPIRY_MONTH_INPUT = "input[name='expiry_month']"
    EXPIRY_YEAR_INPUT = "input[name='expiry_year']"
    PAY_CONFIRM_BUTTON = "#submit"

    # Order Confirmation
    ORDER_PLACED_MESSAGE = "p:has-text('Congratulations! Your order has been confirmed!')"
    SUCCESS_MESSAGE = ".alert-success"
    DOWNLOAD_INVOICE_BUTTON = "a[href='/download_invoice']"
    CONTINUE_BUTTON = "a[data-qa='continue-button']"

    def __init__(self, page):
        super().__init__(page)

    @allure.step("Verify delivery address is displayed")
    def is_delivery_address_visible(self) -> bool:
        """Check if delivery address is visible"""
        return self.is_visible(self.ADDRESS_DELIVERY)

    @allure.step("Verify invoice address is displayed")
    def is_invoice_address_visible(self) -> bool:
        """Check if invoice address is visible"""
        return self.is_visible(self.ADDRESS_INVOICE)

    @allure.step("Add comment to order: {comment}")
    def add_order_comment(self, comment: str):
        """Add comment/note to the order"""
        self.fill(self.COMMENT_TEXTAREA, comment)

    @allure.step("Click Place Order button")
    def click_place_order(self):
        """Click on Place Order button"""
        self.click(self.PLACE_ORDER_BUTTON)

    @allure.step("Fill payment information")
    def fill_payment_information(self, name_on_card: str, card_number: str,
                                 cvc: str, expiry_month: str, expiry_year: str):
        """Fill payment form"""
        self.fill(self.NAME_ON_CARD_INPUT, name_on_card)
        self.fill(self.CARD_NUMBER_INPUT, card_number)
        self.fill(self.CVC_INPUT, cvc)
        self.fill(self.EXPIRY_MONTH_INPUT, expiry_month)
        self.fill(self.EXPIRY_YEAR_INPUT, expiry_year)

    @allure.step("Click Pay and Confirm Order button")
    def click_pay_and_confirm(self):
        """Click on Pay and Confirm Order button"""
        self.click(self.PAY_CONFIRM_BUTTON)

    @allure.step("Verify order is placed successfully")
    def is_order_placed(self) -> bool:
        """Check if order was placed successfully"""
        try:
            self.wait_for_element(self.ORDER_PLACED_MESSAGE, timeout=15000)
            return True
        except:
            return False

    @allure.step("Complete checkout process")
    def complete_checkout(self, payment_data: dict, comment: str = ""):
        """Complete full checkout process"""
        # Verify addresses
        assert self.is_delivery_address_visible(), "Delivery address not visible"
        assert self.is_invoice_address_visible(), "Invoice address not visible"

        # Add comment if provided
        if comment:
            self.add_order_comment(comment)

        self.take_screenshot("before_checkout")

        # Place order
        self.click_place_order()
        self.wait_for_element(self.NAME_ON_CARD_INPUT)

        # Fill payment
        self.fill_payment_information(
            payment_data['name_on_card'],
            payment_data['card_number'],
            payment_data['cvc'],
            payment_data['expiry_month'],
            payment_data['expiry_year']
        )

        self.take_screenshot("payment_filled")

        # Confirm payment
        self.click_pay_and_confirm()

        # Verify order placed
        self.wait_for_element(self.ORDER_PLACED_MESSAGE, timeout=15000)
        self.take_screenshot("order_placed")

    @allure.step("Get order confirmation message")
    def get_confirmation_message(self) -> str:
        """Get order confirmation message"""
        return self.get_text(self.ORDER_PLACED_MESSAGE)