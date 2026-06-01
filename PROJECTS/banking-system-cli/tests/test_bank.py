from app.models.bank import Bank

def test_create_customer():

    bank = Bank()

    customer = bank.create_customer(
        "Brian",
        "Doe"
    )

    assert customer.customer_id in bank.customers


def test_create_account():

    bank = Bank()

    customer = bank.create_customer(
        "Brian",
        "Doe"
    )

    account = bank.create_account(
        customer,
        "1234"
    )

    assert (
        account.account_number in bank.accounts
    )


def test_find_account():
    
    bank = Bank()

    customer = bank.create_customer(
        "Brian",
        "Doe"
    )

    account = bank.create_account(
        customer,
        "1234"
    )

    found = bank.find_account(account.account_number
    )

    assert found == account


def test_authentication():

    bank = Bank()

    customer = bank.create_customer(
        "Brian",
        "Doe"
    )

    account = bank.create_account(
        customer,
        "1234"
    )

    authenticated = bank.authenticate(
        account.account_number,
        "1234"
    )

    assert authenticated == account