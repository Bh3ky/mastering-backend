from app.models.bank_account import BankAccount

class CurrentAccount(BankAccount):
    def __init__(
            self,
            owner: str,
            balance: float,
            overdraft_limit: float
    ):
        super().__init__(owner, balance)

        self.overdraft_limit = overdraft_limit

    
    def withdraw(self, amount:float):
        self._validate_amount(amount)

        allowed_amount = (
            self.balance + self.overdraft_limit
        )

        if amount > allowed_amount:
            raise ValueError(
                "Overdraft limit exceeded."
            )
        
        self._balance -= amount

        self._add_transaction(
            "current amount withdrawal",
            amount
        )