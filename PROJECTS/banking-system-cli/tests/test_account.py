"""
Tests for BankAccount model."""

import pytest
from app.models.customer import Customer
from app.models.account import BankAccount



def create_test_account():

    customer = Customer(
        "Brian",
        "Doe"
    )

    account = BankAccount(
        owner=customer,
        pin="1234"
    )

    return account


def test_deposit():
    account = create_test_account()

    account.deposit(100)

    assert account.balance == 100


def test_withdraw():
    account = create_test_account()

    account.deposit(200)

    account.withdraw(50)

    assert account.balance == 150


def test_invalid_deposit():
    account = create_test_account()

    with pytest.raises(ValueError):
        account.deposit(-50)


def test_pin_verification():
    account = create_test_account()

    assert account.verify_pin("1234") is True

    assert account.verify_pin("9999") is False


def test_account_locking():
    account = create_test_account()

    account.verify_pin("1")
    account.verify_pin("2")
    account.verify_pin("3")

    assert account.is_locked is True