# Automation Exercise - E2E Testing Framework

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-7.4.3-green.svg)](https://pytest.org/)
[![Playwright](https://img.shields.io/badge/Playwright-1.40.0-red.svg)](https://playwright.dev/)
[![Allure](https://img.shields.io/badge/Allure-2.13.2-yellow.svg)](https://docs.qameta.io/allure/)

## 📋 Project Overview

This is a comprehensive automated testing framework for [Automation Exercise](https://www.automationexercise.com/) web application. The framework implements the **Page Object Model (POM)** pattern using **Python**, **Pytest**, and **Playwright** with **Allure** reporting.

### 🎯 Test Coverage

The framework automates the complete user journey:

1. ✅ **User Registration** - Complete signup flow with form validation
2. ✅ **Product Selection** - Browse and add products to cart
3. ✅ **Cart Management** - Verify cart contents and quantities
4. ✅ **Checkout Process** - Complete purchase with payment details

## 🏗️ Project Structure

```
automation_exercise_tests/
│
├── pages/                          # Page Object Model classes
│   ├── __init__.py
│   ├── base_page.py               # Base class with common methods
│   ├── home_page.py               # Home page objects
│   ├── signup_login_page.py       # Registration/Login page objects
│   ├── products_page.py           # Products listing page objects
│   ├── cart_page.py               # Shopping cart page objects
│   └── checkout_page.py           # Checkout and payment page objects
│
├── tests/                         # Test cases
│   ├── __init__.py
│   └── test_e2e_purchase_flow.py  # End-to-end test scenarios
│
├── utils/                         # Utility functions
│   ├── __init__.py
│   └── test_data.py               # Test data generators (Faker)
│
├── reports/                       # Test reports directory
│   ├── allure-results/           # Allure raw results
│   └── videos/                   # Test execution videos
│
├── conftest.py                    # Pytest fixtures and configuration
├── pytest.ini                     # Pytest settings
├── requirements.txt               # Python dependencies
├── .gitignore                     # Git ignore file
└── README.md                      # This file
```

## 🔧 Technical Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.9+** | Programming language |
| **Pytest** | Testing framework |
| **Playwright** | Browser automation |
| **Allure** | Test reporting |
| **Faker** | Test data generation |

## 📦 Installation

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git

### Setup Steps

1. **Clone the repository**
```bash
git clone <your-repository-url>
cd automation_exercise_tests
```

2. **Create virtual environment** (recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Install Playwright browsers**
```bash
playwright install chromium
```

5. **Install Allure** (for report generation)

**On macOS:**
```bash
brew install allure
```

**On Windows:**
```bash
scoop install allure
```

**On Linux:**
```bash
# Download from https://github.com/allure-framework/allure2/releases
# Extract and add to PATH
```

## 🚀 Running Tests

### Run All Tests
```bash
pytest
```

### Run Specific Test File
```bash
pytest tests/test_e2e_purchase_flow.py
```

### Run Tests with Markers
```bash
# Run smoke tests only
pytest -m smoke

# Run cart tests only
pytest -m cart

# Run regression tests
pytest -m regression
```

### Run Tests in Headless Mode
```bash
pytest --headed=false
```

### Run Tests with Specific Browser
```bash
# Chromium (default)
pytest --browser chromium

# Firefox
pytest --browser firefox

# WebKit
pytest --browser webkit
```

### Run Tests in Parallel (requires pytest-xdist)
```bash
pip install pytest-xdist
pytest -n 4  # Run with 4 workers
```

## 📊 Generating Reports

### Allure Reports

1. **Generate and open report**
```bash
allure serve reports/allure-results
```

2. **Generate static report**
```bash
allure generate reports/allure-results -o reports/allure-report --clean
```

3. **Open generated report**
```bash
allure open reports/allure-report
```

### Allure Report Features

- ✅ Test execution timeline
- ✅ Test categorization by features
- ✅ Screenshots on failures
- ✅ Step-by-step execution details
- ✅ Test statistics and trends
- ✅ Video recordings (if enabled)

## 🧪 Test Scenarios

### 1. Complete Purchase Flow Test
**File:** `tests/test_e2e_purchase_flow.py::TestCompletePurchaseFlow::test_complete_purchase_flow`

**Steps:**
1. Open home page
2. Navigate to Signup/Login
3. Register new user with random data
4. Verify successful registration
5. Navigate to Products page
6. Add Product 1 to cart
7. Continue shopping
8. Add Product 2 to cart
9. View cart
10. Verify 2 products in cart
11. Verify product details (name, price, quantity, total)
12. Proceed to checkout
13. Verify delivery and invoice addresses
14. Add order comment
15. Place order
16. Fill payment details
17. Confirm payment
18. Verify order confirmation

**Expected Result:** Order placed successfully with confirmation message

### 2. User Registration Test
**File:** `tests/test_e2e_purchase_flow.py::TestUserRegistration::test_user_registration`

**Steps:**
1. Navigate to signup page
2. Fill registration form
3. Verify successful registration

### 3. Add to Cart Test
**File:** `tests/test_e2e_purchase_flow.py::TestAddToCart::test_add_products_to_cart`

**Steps:**
1. Navigate to products page
2. Add 2 products to cart
3. Verify cart contents

## 📝 Page Object Model (POM)

### Base Page
Contains common methods used across all pages:
- `navigate_to()` - Navigate to URL
- `click()` - Click element
- `fill()` - Fill form field
- `get_text()` - Get element text
- `is_visible()` - Check visibility
- `take_screenshot()` - Capture screenshot
- `scroll_to_element()` - Scroll to element
- `select_dropdown()` - Select from dropdown

### Home Page
- Navigation to Signup/Login
- Navigation to Products
- Navigation to Cart
- User login verification
- Logout functionality

### Signup/Login Page
- User registration
- Account information form
- Address information form
- Account creation verification

### Products Page
- Product listing
- Add to cart functionality
- Continue shopping
- View cart from modal

### Cart Page
- View cart items
- Get product details (name, price, quantity, total)
- Verify cart contents
- Proceed to checkout

### Checkout Page
- Address verification
- Add order comments
- Payment form
- Order confirmation

## 🎨 Features

### ✨ Key Features

1. **Page Object Model (POM)**
   - Clean separation of test logic and page interactions
   - Reusable page methods
   - Easy maintenance

2. **Allure Integration**
   - Detailed test reports
   - Step-by-step execution
   - Screenshots and attachments
   - Test categorization

3. **Dynamic Test Data**
   - Faker library for realistic data
   - Random user generation
   - Unique email addresses

4. **Flexible Configuration**
   - pytest.ini for test settings
   - Configurable browser options
   - Adjustable timeouts and delays

5. **Error Handling**
   - Screenshots on failure
   - Detailed error messages
   - Video recording support

## 🔍 Configuration

### pytest.ini
Configure test execution behavior:
- Test discovery patterns
- Playwright browser settings
- Allure report directory
- Test markers

### conftest.py
Define fixtures and hooks:
- Page object fixtures
- Test data fixtures
- Browser configuration
- Screenshot on failure

## 🐛 Troubleshooting

### Common Issues

1. **Playwright browsers not installed**
```bash
playwright install
```

2. **Module not found errors**
```bash
pip install -r requirements.txt
```

3. **Allure command not found**
- Install Allure command-line tool
- Add Allure to system PATH

4. **Test timeout errors**
- Increase timeout in pytest.ini
- Check internet connection
- Use `--slowmo` for slower execution

5. **Element not found errors**
- Website structure may have changed
- Update locators in page objects
- Increase wait times

## 📈 CI/CD Integration

### GitHub Actions Example
```yaml
name: Automated Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        playwright install chromium
    
    - name: Run tests
      run: pytest --headed=false
    
    - name: Generate Allure Report
      if: always()
      run: allure generate reports/allure-results
    
    - name: Upload Allure Results
      if: always()
      uses: actions/upload-artifact@v2
      with:
        name: allure-results
        path: reports/allure-results
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Write/update tests
5. Run tests locally
6. Submit a pull request

## 📄 License

This project is for educational purposes as part of a testing course assignment.

## 👨‍💻 Author

**Course:** Risk Analysis & System Testing  
**Assignment:** Automation Testing Implementation  
**Framework:** Python + Pytest + Playwright + Allure

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review Playwright documentation: https://playwright.dev/
3. Review Pytest documentation: https://docs.pytest.org/
4. Review Allure documentation: https://docs.qameta.io/allure/

## 🎯 Task Achievement Checklist

- [x] POM pattern implemented (Python + Pytest + Playwright)
- [x] Registration automation
- [x] Add 2 products to Cart
- [x] Check added products in Cart
- [x] Buy all products in the Cart
- [x] Allure report recording
- [x] GitHub repository ready
- [x] Comprehensive documentation

## 📸 Screenshots

Screenshots are automatically captured at key steps:
- Home page
- Signup page
- User logged in
- Products page
- Products added to cart
- Cart state
- Before checkout
- Payment filled
- Order placed
- Order confirmed

## 🎬 Video Recording

Enable video recording in `conftest.py`:
```python
"record_video_dir": "reports/videos/"
```

Videos are saved for each test execution.

---

**Happy Testing! 🚀**