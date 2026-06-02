"""
Custom exceptions used throughout the banking system application.
"""


class BankingError(Exception):
    """
    Base exception for banking errors.
    """
    pass


class InvalidPinError(BankingError):
    """
    Raised when a PIN is invalid.
    """
    pass


class InsufficientFundsError(BankingError):
    """
    Raised when withdrawal exceeds balance.
    """
    pass

class AccountLockedError(BankingError):
    """
    Raised when account is locked.
    """
    pass

class InvalidAmountError(BankingError):
    """
    Raised when an amount is invalid.
    """
    pass

class ValidationError(BankingError):
    """
    Generic validation error.
    """
    pass