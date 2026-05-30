from app.models.payment_method import PaymentMethod

class PayPalPayment(PaymentMethod):
    def process_payment(self):
        print(
            f"Processing PayPal payment "
            f"of ${self.amount}"
        )