class Bank:
    def __init__(self, name: str):
        self.name = name
        self.accounts = []


    def add_account(self, account):
        self.accounts.append(account)


    def show_all_accounts(self):
        print(f"\nAccounts in {self.name}")

        for account in self.accounts:
            print(
                f"{account.account_number} | "
                f"{account.owner} | "
                f"${account.balance}"
            )