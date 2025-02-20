from datetime import datetime
from pydantic import BaseModel, field_validator
from typing import Literal

class Transaction(BaseModel):
    transaction_id: str
    amount: float
    timestamp: datetime
    transaction_type: Literal["deposit", "withdrawal", "transfer"]
    account_from: str
    account_to: str

    @field_validator("amount")
    @classmethod
    def validate_amount(cls, value):
        if value <= 0:
            raise ValueError("Transaction amount must be greater than 0.")
        return round(value, 2)

    @field_validator("account_from", "account_to")
    @classmethod
    def validate_accounts(cls, value):
        if len(value) != 10:
            raise ValueError("Invalid account format. Must be 10 alphanumeric characters.")
        return value

    @field_validator("account_to")
    @classmethod
    def check_transfer_accounts(cls, value, values):
        """Ensure the sender and receiver accounts are not the same."""
        account_from = values.data.get("account_from")  # Access account_from correctly
        if account_from == value:
            raise ValueError("Cannot transfer to the same account.")
        return value


