from app.models.bank import Bank

def main():

    bank = Bank()

    customer = bank.create_customer(
        "Brian",
        "Doe"
    )

    account = bank.create_account(
        customer,
        "1234"
    )

    account.deposit(500)

    print(account)


if __name__ == "__main__":
    main()