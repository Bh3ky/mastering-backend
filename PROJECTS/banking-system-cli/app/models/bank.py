"""
bank.py

Central banking system coordinator.

Responsibilities:
- manage customers
- manage accounts
- authenticate users
- provide account lookup
"""

from app.models.customer import Customer
from app.models.account import BankAccount


class Bank:
    """
    Represents the banking institution.

    Acts as the aggregate root for customers and accounts
    """

    def __init__(self) -> None:
        
        # customer storage
        # key: customer_id
        self.customers = {}

        # account storage
        # key: account_number
        self.accounts ={}


    def create_customer(
            self,
            first_name: str,
            last_name: str
    ) -> Customer:
        """
        Create and register a new customer.
        """

        customer = Customer(
            first_name=first_name,
            last_name=last_name
        )

        self.customers[
            customer.customer_id
        ] = customer

        return customer
    

    def create_account(
            self,
            customer: Customer,
            pin: str
    ) -> BankAccount:
        """
        Create account for an existing customer.
        """

        account = BankAccount(
            owner=customer,
            pin=pin
        )

        customer.add_account(account)

        self.accounts[
            account.account_number
        ] = account

        return account
    

    def find_account(
            self,
            account_number: str
    ) -> BankAccount | None:
        """
        Retrieve account by account number.
        """

        return self.accounts.get(
            account_number
        )
    

    def authenticate(
            self,
            account_number: str,
            pin: str
    ) -> BankAccount | None:
        """
        Authenticate account holder.

        Returns:
            BankAccount if successful
            None if unsuccessful
        """

        account = self.find_account(
            account_number
        )

        if account is None:
            return None
        
        if account.verify_pin(pin):
            return account
        
        return None