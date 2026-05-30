from app.models.credit_card_payment import ( CreditCardPayment )
from app.models.paypal_payment import ( PayPalPayment )
from app.models.crypto_payment import ( CryptoPayment )
from app.models.bank_transfer_payment import ( BankTransferPayment)
from app.services.payment_processor import ( PaymentProcessor )

processor = PaymentProcessor()

payments = [
    CreditCardPayment(500),
    PayPalPayment(300),
    CryptoPayment(1000),
    BankTransferPayment(750)
]

for payment in payments:
    processor.process(payment)