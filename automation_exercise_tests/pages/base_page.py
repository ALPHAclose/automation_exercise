"""
Base Page Object Model class with common methods for all pages
"""
from playwright.sync_api import Page, expect
import allure


class BasePage:
    """Base class for all page objects"""

    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://www.automationexercise.com"

    @allure.step("Navigate to {url}")
    def navigate_to(self, url: str):
        """Navigate to a specific URL"""
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")

    @allure.step("Click element: {locator}")
    def click(self, locator: str):
        """Click on an element"""
        self.page.click(locator)

    @allure.step("Fill field: {locator} with value: {value}")
    def fill(self, locator: str, value: str):
        """Fill a form field"""
        self.page.fill(locator, value)

    @allure.step("Get text from element: {locator}")
    def get_text(self, locator: str) -> str:
        """Get text from an element"""
        return self.page.locator(locator).inner_text()

    @allure.step("Check if element is visible: {locator}")
    def is_visible(self, locator: str) -> bool:
        """Check if element is visible"""
        return self.page.locator(locator).is_visible()

    @allure.step("Wait for element: {locator}")
    def wait_for_element(self, locator: str, timeout: int = 10000):
        """Wait for an element to be visible"""
        self.page.wait_for_selector(locator, timeout=timeout)

    @allure.step("Take screenshot: {name}")
    def take_screenshot(self, name: str):
        """Take a screenshot and attach to Allure report"""
        screenshot = self.page.screenshot()
        allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)

    @allure.step("Scroll to element: {locator}")
    def scroll_to_element(self, locator: str):
        """Scroll to an element"""
        self.page.locator(locator).scroll_into_view_if_needed()

    @allure.step("Select from dropdown: {locator} with value: {value}")
    def select_dropdown(self, locator: str, value: str):
        """Select value from dropdown"""
        self.page.select_option(locator, value)

    @allure.step("Get page title")
    def get_title(self) -> str:
        """Get page title"""
        return self.page.title()

    @allure.step("Assert element text equals: {expected_text}")
    def assert_text_equals(self, locator: str, expected_text: str):
        """Assert that element text equals expected text"""
        expect(self.page.locator(locator)).to_have_text(expected_text)

    @allure.step("Assert element contains text: {expected_text}")
    def assert_text_contains(self, locator: str, expected_text: str):
        """Assert that element text contains expected text"""
        expect(self.page.locator(locator)).to_contain_text(expected_text)