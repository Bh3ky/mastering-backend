from app.models.transaction import Transaction

class BankAccount:
    account_count = 1000


    def __init__(self, owner: str, balance: float):
        BankAccount.account_count += 1

        self.account_number = f"ACC{BankAccount.account_count}"
        self.owner = owner
        self._balance = balance
        # self.transaction_count = 0
        self.transactions = []


    @property
    def balance(self):
        return self._balance
    

    def deposit(self, amount: float):
        self._validate_amount(amount)

        self._balance += amount
        
        self._add_transaction("deposit", amount)


    def withdraw(self, amount: float):
        self._validate_amount(amount)

        if amount > self._balance:
            raise ValueError("Insufficient funds")

        self._balance -= amount

        self._add_transaction("withdrawal", amount)


    def transfer(self, target_account, amount: float):
        self.withdraw(amount)
        target_account.deposit(amount)


    def _validate_amount(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        
    
    def _add_transaction(self, transaction_type, amount):
        transaction = Transaction(transaction_type, amount)
        self.transactions.append(transaction)


    def show_transactions(self):
        print(f"\nTransaction for {self.owner}")

        for transaction in self.transactions:
            print(transaction)
        

    def __str__(self):
        return (
            f"{self.account_number} |"
            f"{self.owner} | "
            f"Balance: ${self.balance}"
        )