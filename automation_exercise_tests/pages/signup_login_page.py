"""
Signup/Login Page Object Model
"""
from pages.base_page import BasePage
import allure


class SignupLoginPage(BasePage):
    """Signup and Login page object with locators and methods"""

    # Locators - New User Signup
    SIGNUP_NAME_INPUT = "input[data-qa='signup-name']"
    SIGNUP_EMAIL_INPUT = "input[data-qa='signup-email']"
    SIGNUP_BUTTON = "button[data-qa='signup-button']"

    # Locators - Login
    LOGIN_EMAIL_INPUT = "input[data-qa='login-email']"
    LOGIN_PASSWORD_INPUT = "input[data-qa='login-password']"
    LOGIN_BUTTON = "button[data-qa='login-button']"

    # Locators - Account Information Form
    GENDER_MR_RADIO = "#id_gender1"
    GENDER_MRS_RADIO = "#id_gender2"
    PASSWORD_INPUT = "#password"
    DAY_DROPDOWN = "#days"
    MONTH_DROPDOWN = "#months"
    YEAR_DROPDOWN = "#years"
    NEWSLETTER_CHECKBOX = "#newsletter"
    OFFERS_CHECKBOX = "#optin"

    # Address Information
    FIRST_NAME_INPUT = "#first_name"
    LAST_NAME_INPUT = "#last_name"
    COMPANY_INPUT = "#company"
    ADDRESS1_INPUT = "#address1"
    ADDRESS2_INPUT = "#address2"
    COUNTRY_DROPDOWN = "#country"
    STATE_INPUT = "#state"
    CITY_INPUT = "#city"
    ZIPCODE_INPUT = "#zipcode"
    MOBILE_INPUT = "#mobile_number"

    CREATE_ACCOUNT_BUTTON = "button[data-qa='create-account']"

    # Account Created Page
    ACCOUNT_CREATED_MESSAGE = "h2[data-qa='account-created']"
    CONTINUE_BUTTON = "a[data-qa='continue-button']"

    def __init__(self, page):
        super().__init__(page)

    @allure.step("Fill signup form with name: {name} and email: {email}")
    def fill_signup_form(self, name: str, email: str):
        """Fill the signup form"""
        self.fill(self.SIGNUP_NAME_INPUT, name)
        self.fill(self.SIGNUP_EMAIL_INPUT, email)
        self.click(self.SIGNUP_BUTTON)

    @allure.step("Fill account information")
    def fill_account_information(self, password: str, day: str, month: str, year: str):
        """Fill account information form"""
        self.click(self.GENDER_MR_RADIO)
        self.fill(self.PASSWORD_INPUT, password)
        self.select_dropdown(self.DAY_DROPDOWN, day)
        self.select_dropdown(self.MONTH_DROPDOWN, month)
        self.select_dropdown(self.YEAR_DROPDOWN, year)
        self.click(self.NEWSLETTER_CHECKBOX)
        self.click(self.OFFERS_CHECKBOX)

    @allure.step("Fill address information")
    def fill_address_information(self, first_name: str, last_name: str, company: str,
                                 address1: str, address2: str, country: str,
                                 state: str, city: str, zipcode: str, mobile: str):
        """Fill address information form"""
        self.fill(self.FIRST_NAME_INPUT, first_name)
        self.fill(self.LAST_NAME_INPUT, last_name)
        self.fill(self.COMPANY_INPUT, company)
        self.fill(self.ADDRESS1_INPUT, address1)
        self.fill(self.ADDRESS2_INPUT, address2)
        self.select_dropdown(self.COUNTRY_DROPDOWN, country)
        self.fill(self.STATE_INPUT, state)
        self.fill(self.CITY_INPUT, city)
        self.fill(self.ZIPCODE_INPUT, zipcode)
        self.fill(self.MOBILE_INPUT, mobile)

    @allure.step("Click Create Account button")
    def click_create_account(self):
        """Click on Create Account button"""
        self.click(self.CREATE_ACCOUNT_BUTTON)

    @allure.step("Verify account created")
    def is_account_created(self) -> bool:
        """Check if account was created successfully"""
        return self.is_visible(self.ACCOUNT_CREATED_MESSAGE)

    @allure.step("Click Continue button")
    def click_continue(self):
        """Click on Continue button after account creation"""
        self.click(self.CONTINUE_BUTTON)

    @allure.step("Complete registration process")
    def complete_registration(self, user_data: dict):
        """Complete full registration process"""
        self.fill_signup_form(user_data['name'], user_data['email'])
        self.wait_for_element(self.PASSWORD_INPUT)

        self.fill_account_information(
            user_data['password'],
            user_data['day'],
            user_data['month'],
            user_data['year']
        )

        self.fill_address_information(
            user_data['first_name'],
            user_data['last_name'],
            user_data['company'],
            user_data['address1'],
            user_data['address2'],
            user_data['country'],
            user_data['state'],
            user_data['city'],
            user_data['zipcode'],
            user_data['mobile']
        )

        self.click_create_account()
        self.wait_for_element(self.ACCOUNT_CREATED_MESSAGE)
        self.take_screenshot("account_created")
        self.click_continue()