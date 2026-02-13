"""
Pytest Configuration and Fixtures
"""
import pytest
from playwright.sync_api import Page
from pages import (
    HomePage,
    SignupLoginPage,
    ProductsPage,
    CartPage,
    CheckoutPage
)
from utils import generate_user_data, generate_payment_data
import allure


@pytest.fixture(scope="function")
def home_page(page: Page) -> HomePage:
    """Fixture to provide HomePage instance"""
    return HomePage(page)


@pytest.fixture(scope="function")
def signup_login_page(page: Page) -> SignupLoginPage:
    """Fixture to provide SignupLoginPage instance"""
    return SignupLoginPage(page)


@pytest.fixture(scope="function")
def products_page(page: Page) -> ProductsPage:
    """Fixture to provide ProductsPage instance"""
    return ProductsPage(page)


@pytest.fixture(scope="function")
def cart_page(page: Page) -> CartPage:
    """Fixture to provide CartPage instance"""
    return CartPage(page)


@pytest.fixture(scope="function")
def checkout_page(page: Page) -> CheckoutPage:
    """Fixture to provide CheckoutPage instance"""
    return CheckoutPage(page)


@pytest.fixture(scope="function")
def user_data():
    """Fixture to provide test user data"""
    return generate_user_data()


@pytest.fixture(scope="function")
def payment_data():
    """Fixture to provide payment data"""
    return generate_payment_data()


@pytest.fixture(scope="function")
def browser_context_args(browser_context_args):
    """Configure browser context"""
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
        "record_video_dir": "reports/videos/",
    }


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture screenshots on test failure"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # Get the page fixture if available
        if "page" in item.funcargs:
            page = item.funcargs["page"]
            screenshot = page.screenshot()
            allure.attach(
                screenshot,
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG
            )


def pytest_configure(config):
    """Configure pytest with custom markers"""
    config.addinivalue_line("markers", "smoke: Smoke test cases")
    config.addinivalue_line("markers", "regression: Regression test cases")
    config.addinivalue_line("markers", "cart: Cart functionality tests")
    config.addinivalue_line("markers", "checkout: Checkout process tests")