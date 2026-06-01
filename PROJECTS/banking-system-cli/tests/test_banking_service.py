"""
Tests for BankingService.

These tests verify that the service layer
correctly coordinates operations between
the CLI and the domain models.
"""

from app.services.banking_service import BankingService
import pytest

def create_test_account():
    """
    Helper function used by multiple tests.

    Creates:
    - BankingService
    - Customer
    - Account

    Returns:
        tuple[BankingService, BankAccount]
    """

    service = BankingService()

    account = service.register_customer(
        first_name="Brian",
        last_name="Doe",
        pin="1234"
    )

    return service, account


# test deposit
def test_service_deposit():
    """
    Verify deposits are processed
    through the service layer.
    """

    service, account = create_test_account()

    service.deposit(
        account,
        500
    )

    assert account.balance == 500


# test withdrawal
def test_service_withdraw():
    """
    Verify withdrawals are processed
    through the service layer.
    """

    service, account = create_test_account()

    service.deposit(
        account,
        500
    )

    service.withdraw(
        account,
        200
    )

    assert account.balance == 300


# test balance retrieval
def test_balance_retrieval():
    """
    Verify balance can be retrieved
    through the service layer.
    """

    service, account = create_test_account()

    service.deposit(
        account,
        750
    )

    balance = service.get_balance(
        account
    )

    assert balance == 750


# test login success
def test_balance_retrieval():
    """
    Verify balance can be retrieved
    through the service layer.
    """

    service, account = create_test_account()

    service.deposit(
        account,
        750
    )

    balance = service.get_balance(
        account
    )

    assert balance == 750


# test login failure
def test_login_failure():
    """
    Verify invalid credentials
    fail authentication.
    """

    service, account = create_test_account()

    authenticated_account = service.login(
        account.account_number,
        "9999"
    )

    assert authenticated_account is None


# test invalid deposit
def test_invalid_deposit():

    service, account = create_test_account()

    with pytest.raises(ValueError):
        service.deposit(
            account,
            -100
        )


# test insufficient funds
def test_insufficient_funds():

    service, account = create_test_account()

    with pytest.raises(ValueError):
        service.withdraw(
            account,
            100
        )


# test account locking
def test_account_locks_after_three_failed_attempts():

    service, account = create_test_account()

    service.login(
        account.account_number,
        "0000"
    )

    service.login(
        account.account_number,
        "0000"
    )

    service.login(
        account.account_number,
        "0000"
    )

    assert account.is_locked is True



