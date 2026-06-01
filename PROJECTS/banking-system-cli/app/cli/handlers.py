"""
handlers.py

Contains functions responsible for handling user interactions.
"""

from app.services.banking_service import BankingService


def handle_create_account(
        service: BankingService
) -> None:
    
    print("\n--- Create Account ---")

    first_name = input(
        "First name: "
    )

    last_name = input(
        "Last name: "
    )

    pin = input(
        "Choose 4-digit PIN:"
    )

    account = service.register_customer(
        first_name,
        last_name,
        pin
    )

    print()

    print(
        "Account created successfully!"
    )

    print(
        f"Account Number: "
        f"{account.account_number}"
    )


def handle_login(
        service: BankingService
):
    print("\n--- Login ---")

    account_number = input(
        "Account number: "
    )

    pin = input(
        "PIN: "
    )

    account = service.login(
        account_number,
        pin
    )

    if account is None:

        print(
            "\nInvalid credentials."
        )

        return None
    
    print(
        f"\nWelcome "
        f"{account.owner.get_full_name()}!"
    )

    return account