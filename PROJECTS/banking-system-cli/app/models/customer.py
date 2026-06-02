"""
customer.py

Contains the Customer class.

A customer can own one or more bank accounts.
"""

from app.utils.generators import generate_customer_id


class Customer:
    """
    Represents a bank customer.
    """

    def __init__(
            self,
            first_name: str,
            last_name: str
    ) -> None:
        
        # unique identifier
        self.customer_id = generate_customer_id()

        # personal details
        self.first_name = first_name
        self.last_name = last_name

        # customer may own multiple accounts
        self.accounts = []

    def add_account(self, account) -> None:
        """
        Link an account to the customer.
        """

        self.accounts.append(account)

    def get_full_name(self) -> str:
        """
        Return customer's full name.
        """

        return f"{self.first_name} {self.last_name}"
    

    def to_dict(self) -> dict:
        """
        Convert customer to dictionary.
        """

        return {
            "customer_id": self.customer_id,
            "first_name": self.first_name,
            "last_name": self.last_name
        }
    
    def __str__(self) -> str:
        """
        Human-readable representation.
        """

        return (
            f"Customer("
            f"id={self.customer_id}, "
            f"name={self.get_full_name()}"
            f")"
        )