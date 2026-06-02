"""
handlers.py

Contains functions responsible for handling user interactions.
"""

from app.services.banking_service import BankingService

from app.validators.validators import (
    validate_name,
    validate_pin
)

from app.exceptions.banking_exceptions import (
    ValidationError
)


def handle_create_account(
        service: BankingService
) -> None:
    
    try:
    
        print("\n--- Create Account ---")

        first_name = validate_name(
            input("First name: ")
        )

        last_name = validate_name(
            input("Last name: ")
        )

        pin = validate_pin(
            input("Choose 4-digit PIN: ")
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

    except ValidationError as error:

        print(
            f"\nValidation Error: {error}"
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