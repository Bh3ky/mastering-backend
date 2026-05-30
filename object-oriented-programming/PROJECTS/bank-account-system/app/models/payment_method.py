class PaymentMethod:
    def __init__(self, amount: float):
        self.amount = amount

        def process_payment(self):
            raise NotImplementedError(
                "Subclasses must implement process_payment()"
            )