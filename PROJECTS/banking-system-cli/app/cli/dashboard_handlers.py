"""
dashboard_handlers.py

Handler for authenticated user.
"""

from app.models.account import BankAccount
from app.services.banking_service import (
    BankingService
)


# deposit handler
def handle_deposit(
    service: BankingService,
    account: BankAccount
) -> None:

    try:

        amount = float(
            input(
                "Enter amount to deposit: "
            )
        )

        service.deposit(
            account,
            amount
        )

        print(
            f"\nDeposit successful."
        )

        print(
            f"New Balance: "
            f"${account.balance}"
        )

    except ValueError as error:

        print(
            f"\nError: {error}"
        )


# withdrawal handler
def handle_withdraw(
    service: BankingService,
    account: BankAccount
) -> None:

    try:

        amount = float(
            input(
                "Enter amount to withdraw: "
            )
        )

        service.withdraw(
            account,
            amount
        )

        print(
            "\nWithdrawal successful."
        )

        print(
            f"New Balance: "
            f"${account.balance}"
        )

    except ValueError as error:

        print(
            f"\nError: {error}"
        )


# balance handler
def handle_balance(
    service: BankingService,
    account: BankAccount
) -> None:

    balance = service.get_balance(
        account
    )

    print(
        f"\nCurrent Balance: "
        f"${balance}"
    )


# transaction handler
def handle_transactions(
    service: BankingService,
    account: BankAccount
) -> None:

    transactions = (
        service.get_transactions(
            account
        )
    )

    print("\nTransaction History")

    print("-" * 40)

    if not transactions:

        print(
            "No transactions found."
        )

        return

    for transaction in transactions:

        print(
            f"{transaction['type']:<15}"
            f"${transaction['amount']}"
        )