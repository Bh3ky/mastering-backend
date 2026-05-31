from app.models.payment_method import PaymentMethod


class CreditCardPayment(PaymentMethod):
    PROCESSING_FEE_PERCENT = 3

    def process_payment(self):
        print(
            f"Processing credit card payment "
            f" of ${self.amount}"
        )

    def calculate_fee(self):
        return (
            self.amount *
            self.PROCESSING_FEE_PERCENT / 100
        )
    
    def generate_receipt(self):
        return (
            f"""
----- CREDIT CARD RECEIPT -----
Amount: ${self.amount}
Fee: ${self.calculate_fee()}
"""
        )
