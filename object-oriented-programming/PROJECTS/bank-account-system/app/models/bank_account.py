from app.models.transaction import Transaction

class BankAccount:
    account_count = 1000


    def __init__(self, owner: str, balance: float):
        BankAccount.account_count += 1

        self.account_number = f"ACC{BankAccount.account_count}"
        self.owner = owner
        self._balance = balance
        self.transaction_count = 0
        self.transactions = []


    @property
    def balance(self):
        return self._balance
    

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        
        self._balance += amount
        self.transaction_count += 1

        transaction = Transaction("deposit", amount)
        self.transactions.append(transaction)


    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        
        self._balance -= amount
        self.transaction_count += 1

        transaction = Transaction("withdraw", amount)
        self.transactions.append(transaction)


    def transfer(self, target_account, amount: float):
        self.withdraw(amount)
        target_account.deposit(amount)
        

    def display_balance(self):
        print(
            f"{self.owner} "
            f"({self.account_number}) "
            f"has ${self._balance}"
        )


    def show_transactions(self):
        print(f"\nTransaction History for {self.owner}")

        for transaction in self.transactions:
            print(transaction)