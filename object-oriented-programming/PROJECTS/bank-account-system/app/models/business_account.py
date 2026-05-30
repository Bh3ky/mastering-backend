from app.models.bank_account import BankAccount

class BusinessAccount(BankAccount):
    WITHDRAWAL_FEE = 5

    def withdraw(self, amount: float):
        total_amount = amount + self.WITHDRAWAL_FEE

        super().withdraw(total_amount)

        self._add_transaction(
            "withdrawal fee",
            self.WITHDRAWAL_FEE
        )