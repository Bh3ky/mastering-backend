"""
generator.py

Contains helper functions responsible for generating unique identifiers used throughout
this application.

Keeping this logic seperate prevents duplication and makes future changes easier.
"""

from uuid import uuid4
import random

def generate_customer_id() -> str:
    """
    Generate a unique customer identifier.
    
    E.g.,: CUST-8f9a12
    """

    return f"CUST-{str(uuid4())[:6]}"

def generate_account_number() -> str:
    """
    Generate a pseudo-random account number.
    
    E.g.,: 10045678
    """

    return str(random.randint(10000000, 99999999))