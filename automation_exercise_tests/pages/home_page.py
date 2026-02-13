"""
Home Page Object Model
"""
from pages.base_page import BasePage
import allure


class HomePage(BasePage):
    """Home page object with locators and methods"""

    # Locators
    SIGNUP_LOGIN_LINK = "a[href='/login']"
    PRODUCTS_LINK = "a[href='/products']"
    CART_LINK = "a[href='/view_cart']"
    HOME_LINK = "a[href='/']"
    LOGGED_IN_USER = "a:has-text('Logged in as')"
    DELETE_ACCOUNT_LINK = "a[href='/delete_account']"
    LOGOUT_LINK = "a[href='/logout']"

    def __init__(self, page):
        super().__init__(page)

    @allure.step("Open home page")
    def open(self):
        """Navigate to home page"""
        self.navigate_to(self.base_url)
        return self

    @allure.step("Click Signup/Login link")
    def click_signup_login(self):
        """Click on Signup/Login link"""
        self.click(self.SIGNUP_LOGIN_LINK)

    @allure.step("Click Products link")
    def click_products(self):
        """Click on Products link"""
        self.click(self.PRODUCTS_LINK)

    @allure.step("Click Cart link")
    def click_cart(self):
        """Click on Cart link"""
        self.click(self.CART_LINK)

    @allure.step("Verify user is logged in as: {username}")
    def is_user_logged_in(self, username: str) -> bool:
        """Check if user is logged in"""
        try:
            logged_in_text = self.get_text(self.LOGGED_IN_USER)
            return username in logged_in_text
        except:
            return False

    @allure.step("Click Logout link")
    def click_logout(self):
        """Click on Logout link"""
        self.click(self.LOGOUT_LINK)

    @allure.step("Click Delete Account link")
    def click_delete_account(self):
        """Click on Delete Account link"""
        self.click(self.DELETE_ACCOUNT_LINK)