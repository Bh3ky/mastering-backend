from app.models.customer import Customer
from app.models.account import BankAccount

def main():

    customer = Customer(
        first_name="Brian",
        last_name="Doe"
    )

    account = BankAccount(
        owner=customer,
        pin="1234"
    )

    customer.add_account(account)

    account.deposit(500)

    account.withdraw(100)

    print(account)

    print("Transactions:")

    for transaction in account.transactions:
        print(transaction)

if __name__ == "__main__":
    main()