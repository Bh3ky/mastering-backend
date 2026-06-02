"""
account.py

Contains the BankAccount class.

Responsibilities:
- store account information
- manage account balance
- authenticate users via PIN
- record transaction
"""

from datetime import datetime

from app.utils.generators import generate_account_number

from app.exceptions.banking_exceptions import (
    InvalidAmountError,
    InsufficientFundsError
)


class BankAccount:
    """
    Represents a bank account.
    """

    def __init__(
        self,
        owner,
        pin: str,
        initial_balance: float = 0.0
    ) -> None:
        
        # unique account number
        self.account_number = generate_account_number()

        # customer object that owns this account
        self.owner = owner

        # protected attribute
        # should only be accessed through methods
        self._pin = pin

        # current account balance
        self.balance = initial_balance

        # transaction auditt trail
        self.transactions = []

        # security tracking
        self.failed_login_attempts = 0

        self.is_lcoked = False

    
    def verify_pin(self, entered_pin: str) -> bool:
        """
        Verify account PIN.
        
        Locks account after 3 failed attempts.
        """

        if self.is_lcoked:
            return False
        
        if entered_pin == self._pin:

            # successful login resets failures
            self.failed_login_attempts = 0

            return True
        
        self.failed_login_attempts += 1

        if self.failed_login_attempts >= 3:
            self.is_locked = True

        return False
    

    def deposit(self, amount: float) -> None:
        """
        Deposit money into account.
        """

        if amount <= 0:
            raise InvalidAmountError(
                "Deposit amount must be positive."
            )
        
        self.balance += amount

        self._record_transaction(
            transaction_type="DEPOSIT",
            amount=amount
        )


    def withdraw(self, amount: float) -> None:
        """
        Withdraw money from account.
        """

        if amount <= 0:
            raise InvalidAmountError(
                "Withdrawal amount must be positive."
            )
        
        if amount > self.balance:
            raise InsufficientFundsError(
                "Insufficient funds."
            )
        
        self.balance -= amount

        self._record_transaction(
            transaction_type="WITHDRAWAL",
            amount=amount
        )

    
    def _record_transaction(
            self,
            transaction_type: str,
            amount: float
    ) -> None:
        """
        Internal helper method.
        
        Records transaction activity.
        """

        self.transactions.append(
            {
                "type": transaction_type,
                "amount": amount,
                "balance_after": self.balance,
                "timestamp": datetime.now().isoformat()
            }
        )

    
    def get_balance(self) -> float:
        """
        Return account balance."""

        return self.balance
    

    def to_dict(self) -> dict:
        """
        Convert account to dictionary.
        """

        return {
            "account_number": self.account_number,
            "customer_id": (
                self.owner.customer_id
            ),
            "balance": self.balance,
            "pin": self._pin,
            "transactions": self.transactions,
            "is_locked": self.is_lcoked,
            "failed_login_attempts": self.failed_login_attempts
        }
    

    def __str__(self) -> str:
        """
        Human-readable representation.
        """

        return(
            f"Account("
            f"number={self.account_number}, "
            f"owner={self.owner.get_full_name()}, "
            f"balance=${self.balance}"
            f")"
        )
