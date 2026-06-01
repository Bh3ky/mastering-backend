"""
banking_service.py

Application service layer.

Acts as the bridge between the CLI and the domain models.
"""

from app.models.bank import Bank
from app.models.account import BankAccount

class BankingService:

    def __init__(self) -> None:

        # central banking system
        self.bank = Bank()


    def register_customer(
        self,
        first_name: str,
        last_name: str,
        pin: str
    ) -> BankAccount:
        
        """
        Create customer and account.
        """

        customer = self.bank.create_customer(
            first_name,
            last_name
        )

        return self.bank.create_account(
            customer,
            pin
        )


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
    ) -> None:
        """
        Deposit money into account.
        """

        account.deposit(amount)


    def withdraw(
        self,
        account: BankAccount,
        amount: float
    ) -> None:
        
        """
        Withdraw money from account.
        """

        account.withdraw(amount)


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
    

