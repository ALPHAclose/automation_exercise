"""
End-to-End Test: Complete User Journey
Test covers: Registration -> Add Products to Cart -> Verify Cart -> Complete Purchase
"""
import pytest
import allure
from pages import HomePage, SignupLoginPage, ProductsPage, CartPage, CheckoutPage
from utils import get_test_comment


@allure.epic("E-Commerce")
@allure.feature("Complete Purchase Flow")
@allure.story("User Registration and Purchase")
@pytest.mark.smoke
@pytest.mark.regression
class TestCompletePurchaseFlow:
    """Test complete purchase flow from registration to order completion"""

    @allure.title("Complete E2E Test: Registration, Add to Cart, Checkout")
    @allure.description("""
    This test performs a complete end-to-end flow:
    1. Register a new user
    2. Add 2 products to cart
    3. Verify products in cart
    4. Complete checkout and purchase
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_complete_purchase_flow(self, home_page: HomePage,
                                    signup_login_page: SignupLoginPage,
                                    products_page: ProductsPage,
                                    cart_page: CartPage,
                                    checkout_page: CheckoutPage,
                                    user_data: dict,
                                    payment_data: dict):
        """
        Complete purchase flow test
        """

        # Step 1: Navigate to home page
        with allure.step("Step 1: Open home page"):
            home_page.open()
            home_page.take_screenshot("home_page")
            assert "Automation Exercise" in home_page.get_title()

        # Step 2: Navigate to Signup/Login page
        with allure.step("Step 2: Navigate to Signup/Login page"):
            home_page.click_signup_login()
            signup_login_page.take_screenshot("signup_page")

        # Step 3: Complete registration
        with allure.step("Step 3: Register new user"):
            allure.attach(
                f"Name: {user_data['name']}\nEmail: {user_data['email']}",
                name="User Registration Data",
                attachment_type=allure.attachment_type.TEXT
            )

            signup_login_page.complete_registration(user_data)

            # Verify user is logged in
            assert home_page.is_user_logged_in(user_data['name']), \
                "User is not logged in after registration"
            home_page.take_screenshot("user_logged_in")

        # Step 4: Navigate to products page
        with allure.step("Step 4: Navigate to Products page"):
            home_page.click_products()
            assert products_page.is_products_page_loaded(), \
                "Products page is not loaded"
            products_page.take_screenshot("products_page")

        # Step 5: Add 2 products to cart
        with allure.step("Step 5: Add 2 products to cart"):
            product_indices = [1, 2]  # First and second products

            allure.attach(
                f"Adding products at indices: {product_indices}",
                name="Products to Add",
                attachment_type=allure.attachment_type.TEXT
            )

            # Add first product
            products_page.add_product_to_cart(product_indices[0])
            products_page.click_continue_shopping()

            # Add second product
            products_page.add_product_to_cart(product_indices[1])
            products_page.click_view_cart_modal()

        # Step 6: Verify products in cart
        with allure.step("Step 6: Verify products in cart"):
            assert cart_page.verify_cart_items_count(2), \
                "Cart does not contain 2 products"

            # Get all products info
            products_info = cart_page.get_all_products_info()

            # Create detailed cart report
            cart_details = "Cart Contents:\n"
            for idx, product in enumerate(products_info, 1):
                cart_details += f"\nProduct {idx}:\n"
                cart_details += f"  Name: {product['name']}\n"
                cart_details += f"  Price: {product['price']}\n"
                cart_details += f"  Quantity: {product['quantity']}\n"
                cart_details += f"  Total: {product['total']}\n"

            allure.attach(
                cart_details,
                name="Cart Details",
                attachment_type=allure.attachment_type.TEXT
            )

            cart_page.capture_cart_state()

            # Verify cart is not empty
            assert cart_page.is_cart_not_empty(), "Cart is empty"

        # Step 7: Proceed to checkout
        with allure.step("Step 7: Proceed to checkout"):
            cart_page.click_proceed_to_checkout()
            checkout_page.take_screenshot("checkout_page")

        # Step 8: Complete purchase
        with allure.step("Step 8: Complete purchase"):
            order_comment = get_test_comment()

            allure.attach(
                f"Card: {payment_data['card_number']}\n"
                f"Name: {payment_data['name_on_card']}\n"
                f"Expiry: {payment_data['expiry_month']}/{payment_data['expiry_year']}\n"
                f"Comment: {order_comment}",
                name="Payment and Order Details",
                attachment_type=allure.attachment_type.TEXT
            )

            checkout_page.complete_checkout(payment_data, order_comment)

            # Verify order is placed
            assert checkout_page.is_order_placed(), \
                "Order was not placed successfully"

            confirmation_msg = checkout_page.get_confirmation_message()
            allure.attach(
                confirmation_msg,
                name="Order Confirmation Message",
                attachment_type=allure.attachment_type.TEXT
            )

        # Final verification
        with allure.step("Step 9: Final verification"):
            assert "Congratulations" in confirmation_msg, \
                "Order confirmation message not found"
            checkout_page.take_screenshot("order_confirmed")


@allure.epic("E-Commerce")
@allure.feature("User Registration")
@allure.story("New User Signup")
@pytest.mark.smoke
class TestUserRegistration:
    """Test user registration functionality"""

    @allure.title("Register New User Successfully")
    @allure.description("Test user registration with valid data")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_registration(self, home_page: HomePage,
                               signup_login_page: SignupLoginPage,
                               user_data: dict):
        """Test user registration"""

        with allure.step("Navigate to home page and signup"):
            home_page.open()
            home_page.click_signup_login()

        with allure.step("Complete registration form"):
            signup_login_page.complete_registration(user_data)

        with allure.step("Verify registration success"):
            assert home_page.is_user_logged_in(user_data['name']), \
                "User registration failed"


@allure.epic("E-Commerce")
@allure.feature("Shopping Cart")
@allure.story("Add Products to Cart")
@pytest.mark.cart
class TestAddToCart:
    """Test adding products to cart"""

    @allure.title("Add Multiple Products to Cart")
    @allure.description("Test adding 2 products to cart and verify")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_products_to_cart(self, home_page: HomePage,
                                  products_page: ProductsPage,
                                  cart_page: CartPage):
        """Test adding products to cart"""

        with allure.step("Navigate to products page"):
            home_page.open()
            home_page.click_products()

        with allure.step("Add 2 products"):
            products_page.add_product_to_cart(1)
            products_page.click_continue_shopping()
            products_page.add_product_to_cart(2)
            products_page.click_view_cart_modal()

        with allure.step("Verify cart contents"):
            assert cart_page.verify_cart_items_count(2), \
                "Cart item count mismatch"
            cart_page.capture_cart_state()