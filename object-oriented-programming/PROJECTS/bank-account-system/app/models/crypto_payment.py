from app.models.payment_method import PaymentMethod

class CryptoPayment(PaymentMethod):
    PROCESSING_FEE_PERCENT = 1

    def process_payment(self):
        print(
            f"Processing crypto payment "
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
----- CRYPTO RECEIPT -----
Amount: ${self.amount}
Fee: ${self.calculate_fee()}
-----------------------------
"""
        )