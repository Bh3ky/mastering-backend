# Lesson 5 - Polymorphism & Interface-Based Design

**Polymorphism** means different objects can be used through the same interface. 

- e.g., `payment.process_payment()`. the caller doesn't care whether it is a credit card, PayPal, crypto or bank transfer each object knows how to process itself. 

**Question: why is polymorphism importarnt??**
- polymorphism enables:
    - scalable systems
    - plugin architectures
    - payment gateways
    - framework design
    - dependency injection
    - clean APIs

- in this lesson we will build the following on top of our already existing banking system:

```text
PaymentMethod
│
├── CreditCardPayment
├── PayPalPayment
├── CryptoPayment
└── BankTransferPayment
```

- all the aforomentioned expose `process_payment()`.

1. first, we need to create the base payment class first

file: `app/models/payment_method.py`

```python
class PaymentMethod:
    def __init__(self, amount: float):
        self.amount = amount

    def process_payment(self):
        raise NotImplementedError(
            "Subclasses must implement process_payment()"
        )
```

- this class defines:
> a common contract/interface

every payment type must provide: `process_payment()`

- `raise NotImplementedError` means that child classes are required to implement this method.
    - this simulates abstraction/interface behavoir.

2. next we create a credit card payment file

file: `app/models/credit_card_payment.py`

```python
from app.models.payment_method import PaymentMethod


class CreditCardPayment(PaymentMethod):
    def process_payment(self):
        print(
            f"Processing credit card payment "
            f"of ${self.amount}"
        )
```

3. PayPal payment file

file: `app/models/paypal_payment.py`

```python
from app.models.payment_method import PaymentMethod


class PayPalPayment(PaymentMethod):
    def process_payment(self):
        print(
            f"Processing PayPal payment "
            f"of ${self.amount}"
        )
```

4. Crypto payment file

file: `app/models/crypto_payment.py`

```python
from app.models.payment_method import PaymentMethod


class CryptoPayment(PaymentMethod):
    def process_payment(self):
        print(
            f"Processing crypto payment "
            f"of ${self.amount}"
        )
```

5. Bank transfer payment

file: `app/models/bank_transfer_payment.py`

```python
from app.models.payment_method import PaymentMethod


class BankTransferPayment(PaymentMethod):
    def process_payment(self):
        print(
            f"Processing bank transfer "
            f"of ${self.amount}"
        )
```

6. now we build the payment processor

file: `app/services/payment_processor.py`

```python
class PaymentProcessor:
    def process(self, payment_method):
        payment_method.process_payment()
```

- here we have `payment_method.process_payment()`. the processor:
    - doesn't know the exact class
    - doesn't use `if/elif`
    - doesn't care about implementation
- only cares that `process_payment` exists. _polymorphism_.

```text
PaymentProcessor
        ↓
process_payment()
        ↓
--------------------------------
|       |       |       |
Card   PayPal Crypto  Bank
```

7. update `main.py`

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

from app.models.bank_transfer_payment import (
    BankTransferPayment
)

from app.services.payment_processor import (
    PaymentProcessor
)


processor = PaymentProcessor()

payments = [
    CreditCardPayment(500),
    PayPalPayment(300),
    CryptoPayment(1000),
    BankTransferPayment(750)
]

for payment in payments:
    processor.process(payment)
```

- the for loop contains different object types, yet they all work seasmlessly because:
    - they share a common interface
    - they all implement `process_payment()`

**Dynamic Dispatch**
- internally, `payment.process_payment()` runs and Python determines at runtime actual object type and correct method implementation

- polymorphism aligns with the _open/closed principle_ which states that software should be "open for extension & closed for modification"