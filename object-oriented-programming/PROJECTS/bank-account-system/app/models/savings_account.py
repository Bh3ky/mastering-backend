from app.models.bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(
            self,
            owner: str,
            balance: float,
            interest_rate: float
    ):
        super().__init__(owner, balance)

        self.interent_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * (self.interent_rate / 100)

        self._balance += interest

        self._add_transaction("interest", interest)