# Lesson 6 - Abstraction & Abstract Base Classes (ABC)

- previously we used `raise NotImplementedError` to force subclasses to implement methods. it works yeah?? but Python provides a more professional and safer mechanism:

**Abstract Base Classes (ABC)**

- abstraction means exposing essential behaviour while hiding implementation details. for example:
    - we know `payment.process_payment()` but we don't care about how PayPal talks to servers, how crypto signatures work or how banks validate transfers. 
    - the complexity is hidded behind an interface.


**Why Abstraction Matters**
- without abstraction systems become tightly couples, implementation details leak everywhere, and scaling becomes difficult. 
- abstraction allows interchangeable components, cleaner APIs, extensibility, and framework design.


- Note: abstraction focuses on _defining required behaviour/contracts_.

1. firstly, we need to refactor PaymentMethod file

file: `app/models/payment_method.py`

```python
from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    def __init__(self, amount: float):
        self.amount = amount

    @abstractmethod
    def process_payment(self):
        pass

    @abstractmethod
    def calculate_fee(self):
        pass

    @abstractmethod
    def generate_receipt(self):
        pass
```

- `class PaymentMethod(ABC):` marks the class as abstract i.e., incomplete blueprint and cannot be instantiated directly. 

- `@abstractmethod` forces subclasses to implement the method. NB: Python now prevents invalid subclasses immediately.


2. need to update CreditCardPayment, PayPalPayment, CryptoPayment files:

file: `app/models/credit_card_payment.py`

```python
from app.models.payment_method import PaymentMethod


class CreditCardPayment(PaymentMethod):
    PROCESSING_FEE_PERCENT = 3

    def process_payment(self):
        print(
            f"Processing credit card payment "
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
----- CREDIT CARD RECEIPT -----
Amount: ${self.amount}
Fee: ${self.calculate_fee()}
--------------------------------
"""
        )
```

file: `app/models/paypal_payment.py`

```python
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
```

file: `app/models/crypto_payment.py`

```python
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
```

3. need to improve PaymentProcessor file

file: `app/services/payment_processor.py`

```python
class PaymentProcessor:
    def process(self, payment_method):
        payment_method.process_payment()

        receipt = payment_method.generate_receipt()

        print(receipt)
```

- the processor now relies ONLY on abstraction. it doesn't know the implementation details, concrete payment classes, and fee rules. _only trust the contract/interface_.

4. update main.py file:

```python
from app.models.credit_card_payment import (
    CreditCardPayment
)

from app.models.paypal_payment import (
    PayPalPayment
)

from app.models.crypto_payment import (
    CryptoPayment
)

from app.services.payment_processor import (
    PaymentProcessor
)


processor = PaymentProcessor()

payments = [
    CreditCardPayment(1000),
    PayPalPayment(500),
    CryptoPayment(3000)
]

for payment in payments:
    processor.process(payment)
```
