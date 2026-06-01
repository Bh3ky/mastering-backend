"""
dashboard.py

Authenticated user menu.
"""

from app.cli.dashboard_handlers import (
    handle_deposit,
    handle_withdraw,
    handle_balance,
    handle_transactions
)


def display_dashboard(customer_name: str) -> None:

    print("\n" + "=" * 40)
    print(f"Welcome {customer_name}")
    print("=" * 40)

    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. View Transactions")
    print("5. Logout")

    print()

def dashboard_loop(
    service,
    account
) -> None:
    """
    Runs authenticated session.
    """

    while True:

        display_dashboard(
            account.owner.get_full_name()
        )

        choice = input(
            "Select option: "
        )

        if choice == "1":

            handle_deposit(
                service,
                account
            )

        elif choice == "2":

            handle_withdraw(
                service,
                account
            )

        elif choice == "3":

            handle_balance(
                service,
                account
            )

        elif choice == "4":

            handle_transactions(
                service,
                account
            )

        elif choice == "5":

            print(
                "\nLogged out."
            )

            break

        else:

            print(
                "\nInvalid option."
            )