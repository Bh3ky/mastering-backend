from app.models.payment_method import PaymentMethod

class CreditCardPayment(PaymentMethod):
    def process_payment(self):
        print(
            f"Processing credit card payment "
            f"of ${self.amount}"
        )