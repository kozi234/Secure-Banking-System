"""
Title: Transaction Class - Secure Banking System
Author: John A. Kibozi
Course: CSC3028X00
Date: March 8, 2025
Description:
This module defines the Transaction class, which represents a financial transaction
(deposits, withdrawals, transfers). The class uses Pydantic for data validation
and includes methods to ensure valid transaction entries.
"""

from datetime import datetime, timezone
from typing import Literal, Optional
from pydantic import BaseModel, field_validator
import uuid

class Transaction(BaseModel):
    """
    Represents a financial transaction with validation.
    Supports deposits, withdrawals, and transfers.
    """
    transaction_id: str  # Unique identifier for transaction
    amount: float  # Transaction amount
    timestamp: datetime  # Time transaction was created
    transaction_type: Literal["deposit", "withdrawal", "transfer"]  # Type of transaction
    account_from: Optional[str] = None  # Optional for deposits
    account_to: Optional[str] = None  # Optional for withdrawals
    description: Optional[str] = None  # Additional transaction notes

    @field_validator("amount")
    @classmethod
    def validate_amount(cls, value):
        """Ensure the transaction amount is positive and rounded to 2 decimal places."""
        if value <= 0:
            raise ValueError("Transaction amount must be greater than 0.")
        return round(value, 2)

    @field_validator("account_from", "account_to")
    @classmethod
    def validate_accounts(cls, value):
        """Ensure account numbers are valid (10 alphanumeric characters)."""
        if value and len(value) != 10:
            raise ValueError("Invalid account format. Must be 10 alphanumeric characters.")
        return value

    @field_validator("account_to")
    @classmethod
    def check_transfer_accounts(cls, value, values):
        """Ensure sender and receiver accounts are not the same for transfers."""
        account_from = values.data.get("account_from")
        if account_from and account_from == value:
            raise ValueError("Cannot transfer to the same account.")
        return value

    @classmethod
    def create_transaction(cls, amount: float, transaction_type: str, account_from=None, account_to=None, description=None):
        """Factory method to create a transaction with an auto-generated ID and timestamp."""
        return cls(
            transaction_id=str(uuid.uuid4()),  # Auto-generate unique transaction ID
            amount=amount,
            timestamp=datetime.now(timezone.utc),
            transaction_type=transaction_type,
            account_from=account_from,
            account_to=account_to,
            description=description
        )


# Example Usage:
if __name__ == "__main__":
    try:
        # Example of creating a valid deposit transaction
        deposit = Transaction.create_transaction(amount=150.75, transaction_type="deposit")
        print("\nDeposit Transaction:")
        print(deposit)

        # Example of creating a valid transfer transaction
        transfer = Transaction.create_transaction(amount=50.00, transaction_type="transfer", account_from="1234567890", account_to="0987654321")
        print("\nTransfer Transaction:")
        print(transfer)

    except ValueError as e:
        print(f"Transaction error: {e}")