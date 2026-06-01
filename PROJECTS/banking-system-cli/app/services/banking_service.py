"""
banking_service.py

Application service layer.

Coordinates business operations between the CLI and domain models.
"""

from app.models.bank import Bank


class BankingService:

    def __init__(self) -> None:

        # central banking system
        self.bank = Bank()


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

        return account
    

    def login(
            self,
            account_number: str,
            pin: str
    ):
        """
        Authenticate user.
        """

        return self.bank.authenticate(
            account_number,
            pin
        )
    

