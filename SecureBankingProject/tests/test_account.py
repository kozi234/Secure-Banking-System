# SecureBankingProject/tests/test_account.py

import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.account import Account

def test_account_creation():
    account = Account(
        account_id="ACCNT0001A",  # ✅ 10 characters
        account_type="checking",
        owner_id="1001",
        name="Test Account",
        balance=100.0
    )
    assert account.account_type == "checking"

def test_valid_account_creation():
    acc = Account(
        account_id="ACCNT0002B",
        account_type="savings",
        owner_id=1002,
        account_number="1234567890",
        balance=1000.00
    )
    assert acc.owner_id == 1002
    assert acc.balance == 1000.00

def test_negative_balance_raises_error():
    with pytest.raises(ValueError):
        Account(
            account_id="3",
            account_type="savings",
            owner_id="1003",
            account_number="9999999999",
            owner="Jane Doe",
            balance=-50.00
        )
