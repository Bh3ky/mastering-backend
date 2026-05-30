from app.models.payment_method import PaymentMethod

class CryptoPayment(PaymentMethod):
    def process_payment(self):
        print(
            f"Processing crypto payment "
            f"of ${self.amount}"
        )