from app.models.payment_method import PaymentMethod

class BankTransferPayment(PaymentMethod):
    def process_payment(self):
        print(
            f"Processing bank transfer "
            f"of ${self.amount}"
        )