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