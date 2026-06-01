"""
Application entry point.
"""

from app.cli.menu import (
    display_main_menu
)

from app.cli.handlers import (
    handle_create_account,
    handle_login
)

from app.services.banking_service import (
    BankingService
)

from app.cli.dashboard import (
    dashboard_loop
)

def main():

    service = BankingService()
    
    while True:

        display_main_menu()

        choice = input(
            "Select an option: "
        )

        if choice == "1":
            handle_create_account(service)

        elif choice == "2":
            
            account = handle_login(service)

            if account:

                dashboard_loop(
                    service,
                    account
                )

        elif choice == "3":
            print("\nThank you for using CLBANK!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()