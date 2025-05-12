"""
Title: Account Model - Secure Banking System
Author: John A. Kibozi
Course: CSC3028X00
Date: March 10, 2025
Description:
This module defines the Account model for the Secure Banking System.
It ensures account data integrity through strict validation.
"""

import uuid
from typing import Literal, Optional
from pydantic import BaseModel, field_validator


class Account(BaseModel):
    """Represents a bank account with strict validation rules."""
    
    account_id: str  # Unique account identifier
    account_type: Literal["savings", "checking", "investment"]  # Restricted account types
    balance: float  # Account balance (cannot be negative)
    owner_id: int  # ID of the user who owns the account
    description: Optional[str] = None  # Optional description for the account

    @field_validator("account_id")
    @classmethod
    def validate_account_id(cls, value):
        """Ensures the account ID is exactly 10 alphanumeric characters."""
        if not value.isalnum() or len(value) != 10:
            raise ValueError("Account ID must be exactly 10 alphanumeric characters.")
        return value

    @field_validator("balance")
    @classmethod
    def validate_balance(cls, value):
        """Ensures the balance is non-negative and rounds to two decimal places."""
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        return round(value, 2)

    @classmethod
    def create_new_account(cls, account_type: str, owner_id: int, initial_balance: float = 0.0):
        """Creates a new account with a randomly generated account ID."""
        return cls(
            account_id=str(uuid.uuid4().hex[:10]),  # Generate a unique 10-character ID
            account_type=account_type,
            balance=initial_balance,
            owner_id=owner_id
        )


# **Test Case: Creating an Account**
if __name__ == "__main__":
    try:
        new_account = Account.create_new_account("savings", owner_id=12345, initial_balance=500.0)
        print("\n✅ Account Successfully Created:\n", new_account)
    except ValueError as e:
        print(f"❌ Error: {e}")
