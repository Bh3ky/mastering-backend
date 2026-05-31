class PaymentProcessor:
    def process(self, payment_method):
        payment_method.process_payment()

        receipt = payment_method.generate_receipt()

        print(receipt)