from app.models.payment_method import PaymentMethod

class PayPalPayment(PaymentMethod):
    PROCESSING_FEE_PERCENT = 5

    def process_payment(self):
        print(
            f"Processing PayPal payment "
            f"of ${self.amount}"
        )

    def calculate_fee(self):
        return (
            self.amount *
            self.PROCESSING_FEE_PERCENT / 100
        )

    def generate_receipt(self):
        return (
            f"""
----- PAYPAL RECEIPT -----
Amount: ${self.amount}
Fee: ${self.calculate_fee()}
-----------------------------
"""
        )