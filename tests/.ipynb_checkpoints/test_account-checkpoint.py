import sys
import os

# Get the absolute path of the project root directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.user import User  # Import the User model

import pytest
from models.account import Account

def test_valid_account():
    account = Account(
        account_id="123456789A",
        account_type="savings",
        balance=500.75,
        owner_id=1
    )
    assert account.balance == 500.75

def test_invalid_account_id():
    with pytest.raises(ValueError):
        Account(
            account_id="1234",
            account_type="savings",
            balance=500.75,
            owner_id=1
        )

def test_negative_balance():
    with pytest.raises(ValueError):
        Account(
            account_id="987654321B",
            account_type="checking",
            balance=-100.00,
            owner_id=2
        )
