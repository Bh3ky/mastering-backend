"""
Tests for Customer model.
"""

from app.models.customer import Customer

def test_customer_creation():

    customer = Customer(
        first_name="Brian",
        last_name="Doe"
    )

    assert customer.first_name == "Brian"
    assert customer.last_name == "Doe"

    assert len(customer.accounts) == 0

def test_full_name():

    customer = Customer(
        first_name="Brian",
        last_name="Doe"
    )

    assert customer.get_full_name() == "Brian Doe"