# SecureBankingProject/tests/test_transaction.py

import pytest
from datetime import datetime
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.transaction import Transaction


def test_transaction_init():
    txn = Transaction(
        transaction_id="TXN999",
        timestamp=datetime.now(),
        transaction_type="transfer",
        amount=50.0
    )
    assert txn.amount == 50.0
    assert txn.transaction_type == "transfer"

def test_transaction_creation():
    txn = Transaction(
        transaction_id="TXN001",
        amount=200.0,
        timestamp=datetime.now(),
        transaction_type="deposit",
        account_to="1234567890"
    )
    assert txn.amount == 200.0
    assert txn.transaction_type == "deposit"

def test_valid_transfer_transaction():
    tx = Transaction(
        transaction_id="TXN1001",
        amount=150.00,
        timestamp=datetime.now(),
        transaction_type="transfer",
        account_from="1234567890",
        account_to="0987654321"
    )
    assert tx.transaction_id == "TXN1001"
    assert tx.amount == 150.00

def test_invalid_same_account_transfer():
    with pytest.raises(ValueError):
        Transaction(
            transaction_id="TXN1002",
            amount=100.00,
            timestamp=datetime.now(),
            transaction_type="transfer",
            account_from="1111111111",
            account_to="1111111111"
        )
