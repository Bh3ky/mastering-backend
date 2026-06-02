"""
Validation utilities.

All user input should pass through these functions before entering
the domain layer.
"""

from app.exceptions.banking_exceptions import (
    ValidationError
)

# name validation
def validate_name(name: str) -> str:
    """
    Validate first or last name."""

    cleaned_name = name.strip()

    if not cleaned_name:
        raise ValidationError(
            "Name cannot be empty."
        )
    
    if not cleaned_name.isalpha():
        raise ValidationError(
            "Name must contain letters only."
        )
    
    return cleaned_name


# pin validation
def validate_pin(pin: str) -> str:
    """
    Validate account PIN."""

    pin = pin.strip()

    if len(pin) != 4:
        raise ValidationError(
            "PIN must be 4 digits."
        )
    
    if not pin.isdigit():
        raise ValidationError(
            "PIN must contain only numbers."
        )
    
    return pin


# amount validation
def validate_amount(amount: float) -> float:
    """
    Validate monetary amount.
    """

    if amount <= 0:
        raise ValidationError(
            "Amount must be greater than zero."
        )
    
    return amount