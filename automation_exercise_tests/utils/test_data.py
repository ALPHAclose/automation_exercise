"""
Test Data Generator using Faker
"""
from faker import Faker
import random
import string

fake = Faker()


def generate_random_email():
    """Generate a random email address"""
    return fake.email()


def generate_random_password(length=10):
    """Generate a random password"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_user_data():
    """Generate complete user registration data"""
    first_name = fake.first_name()
    last_name = fake.last_name()

    user_data = {
        'name': f"{first_name} {last_name}",
        'email': f"{first_name.lower()}.{last_name.lower()}{random.randint(100, 999)}@testmail.com",
        'password': 'Test@123456',
        'day': str(random.randint(1, 28)),
        'month': str(random.randint(1, 12)),
        'year': str(random.randint(1970, 2000)),
        'first_name': first_name,
        'last_name': last_name,
        'company': fake.company(),
        'address1': fake.street_address(),
        'address2': fake.secondary_address(),
        'country': 'India',
        'state': fake.state(),
        'city': fake.city(),
        'zipcode': fake.zipcode(),
        'mobile': fake.numerify(text='##########')
    }

    return user_data


def generate_payment_data():
    """Generate payment card data"""
    payment_data = {
        'name_on_card': fake.name(),
        'card_number': '4532015112830366',  # Test card number
        'cvc': '123',
        'expiry_month': '12',
        'expiry_year': '2027'
    }

    return payment_data


def get_test_comment():
    """Get a test comment for order"""
    comments = [
        "Please deliver between 9 AM - 5 PM",
        "Handle with care",
        "Gift wrapping required",
        "Leave at the door if no one is home",
        "Call before delivery"
    ]
    return random.choice(comments)