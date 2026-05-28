from datetime import datetime

class Transaction:
    def __init__(self, transaction_type: str, amount: float):
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = datetime.now()

    def __str__(self):
        return (
            f"{self.transaction_type.upper()} | "
            f"${self.amount} | "
            f"{self.timestamp}"
        )