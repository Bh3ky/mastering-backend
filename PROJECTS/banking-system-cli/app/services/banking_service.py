"""
banking_service.py

Application service layer.

Acts as the bridge between the CLI and the domain models.
"""

from app.models.bank import Bank
from app.models.account import BankAccount

from app.storage.json_storage import (
    JsonStorage
)

class BankingService:

    def __init__(self) -> None:

        # central banking system
        self.bank = Bank()


    def save_data(self) -> None:
        """
        Save current bank state.
        """

        JsonStorage.save(
            self.bank.to_dict()
        )


    def register_customer(
        self,
        first_name: str,
        last_name: str,
        pin: str
    ):
        
        """
        Create customer and account.
        """

        customer = self.bank.create_customer(
            first_name,
            last_name
        )

        account = self.bank.create_account(
            customer,
            pin
        )

        # persist newly created customer/account
        self.save_data()

        return account


    def login(
        self,
        account_number: str,
        pin: str
    ) -> BankAccount | None:
        """
        Authenticate user.
        """

        return self.bank.authenticate(
            account_number,
            pin
        )
    

    def deposit(
        self,
        account: BankAccount,
        amount: float
    ):
        """
        Deposit money into account.
        """

        account.deposit(amount)

        # persist updated balance
        self.save_data()


    def withdraw(
        self,
        account: BankAccount,
        amount: float
    ):
        
        """
        Withdraw money from account.
        """

        account.withdraw(amount)

        # persist updated balance
        self.save_data()


    def get_balance(
        self,
        account: BankAccount
    ) -> float:
        
        return account.get_balance()
    

    def get_transactions(
        self,
        account: BankAccount
    ) -> list:
        
        return account.transactions
    

