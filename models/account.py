from typing import Literal
from pydantic import BaseModel, field_validator

class Account(BaseModel):
    account_id: str
    account_type: Literal["savings", "checking", "investment"]
    balance: float
    owner_id: int

    @field_validator("account_id")
    @classmethod
    def validate_account_id(cls, value):
        if not value.isalnum() or len(value) != 10:
            raise ValueError("Account ID must be exactly 10 alphanumeric characters.")
        return value

    @field_validator("balance")
    @classmethod
    def validate_balance(cls, value):
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        return round(value, 2)