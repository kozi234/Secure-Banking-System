{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "4d261def-5177-445a-a2e0-12dfe6c83cf7",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Audit logger initialized.\n",
      "✅ Valid Deposit: transaction_id='TXN001' amount=300.0 timestamp=datetime.datetime(2025, 3, 24, 22, 40, 33, 917663) transaction_type='deposit' account_from=None account_to='1234567890' description=None\n",
      "✅ Valid Transfer: transaction_id='TXN002' amount=200.0 timestamp=datetime.datetime(2025, 3, 24, 22, 40, 33, 918664) transaction_type='transfer' account_from='1234567890' account_to='0987654321' description=None\n",
      "🚫 Negative Amount Test Passed: 1 validation error for Transaction\n",
      "amount\n",
      "  Value error, Transaction amount must be greater than 0. [type=value_error, input_value=-50.0, input_type=float]\n",
      "    For further information visit https://errors.pydantic.dev/2.8/v/value_error\n",
      "🚫 Invalid Account Format Test Passed: 2 validation errors for Transaction\n",
      "account_from\n",
      "  Value error, Invalid account format. Must be 10 alphanumeric characters. [type=value_error, input_value='abc', input_type=str]\n",
      "    For further information visit https://errors.pydantic.dev/2.8/v/value_error\n",
      "account_to\n",
      "  Value error, Invalid account format. Must be 10 alphanumeric characters. [type=value_error, input_value='xyz', input_type=str]\n",
      "    For further information visit https://errors.pydantic.dev/2.8/v/value_error\n",
      "🚫 Same Account Transfer Test Passed: 1 validation error for Transaction\n",
      "account_to\n",
      "  Value error, Cannot transfer to the same account. [type=value_error, input_value='1234567890', input_type=str]\n",
      "    For further information visit https://errors.pydantic.dev/2.8/v/value_error\n",
      "⚠️ Over Limit Transaction: transaction_id='TXN006' amount=6000.0 timestamp=datetime.datetime(2025, 3, 24, 22, 40, 33, 918664) transaction_type='withdrawal' account_from='1234567890' account_to=None description=None\n",
      "❌ Over Limit Test Failed: type object 'datetime.datetime' has no attribute 'datetime'\n"
     ]
    }
   ],
   "source": [
    "import sys, os\n",
    "from datetime import datetime\n",
    "\n",
    "# Add logs and models folder to sys.path\n",
    "base_dir = os.path.abspath(\"..\")\n",
    "sys.path.append(os.path.join(base_dir, \"models\"))\n",
    "sys.path.append(os.path.join(base_dir, \"logs\"))\n",
    "\n",
    "# Now import modules\n",
    "from transaction import Transaction\n",
    "from policy import SecurityPolicy\n",
    "from audit_log import log_event\n",
    "\n",
    "# Test 1: Valid Deposit\n",
    "try:\n",
    "    deposit = Transaction(\n",
    "        transaction_id=\"TXN001\",\n",
    "        amount=300.00,\n",
    "        timestamp=datetime.now(),\n",
    "        transaction_type=\"deposit\",\n",
    "        account_from=None,\n",
    "        account_to=\"1234567890\"\n",
    "    )\n",
    "    print(\"Valid Deposit:\", deposit)\n",
    "except Exception as e:\n",
    "    print(\"Failed Deposit Test:\", e)\n",
    "\n",
    "# Test 2: Valid Transfer\n",
    "try:\n",
    "    transfer = Transaction(\n",
    "        transaction_id=\"TXN002\",\n",
    "        amount=200.00,\n",
    "        timestamp=datetime.now(),\n",
    "        transaction_type=\"transfer\",\n",
    "        account_from=\"1234567890\",\n",
    "        account_to=\"0987654321\"\n",
    "    )\n",
    "    print(\"Valid Transfer:\", transfer)\n",
    "except Exception as e:\n",
    "    print(\"Failed Transfer Test:\", e)\n",
    "\n",
    "# Test 3: Invalid Amount (negative)\n",
    "try:\n",
    "    Transaction(\n",
    "        transaction_id=\"TXN003\",\n",
    "        amount=-50.00,\n",
    "        timestamp=datetime.now(),\n",
    "        transaction_type=\"deposit\",\n",
    "        account_from=None,\n",
    "        account_to=\"1234567890\"\n",
    "    )\n",
    "except Exception as e:\n",
    "    print(\"Negative Amount Test Passed:\", e)\n",
    "\n",
    "# Test 4: Invalid Account Format\n",
    "try:\n",
    "    Transaction(\n",
    "        transaction_id=\"TXN004\",\n",
    "        amount=100,\n",
    "        timestamp=datetime.now(),\n",
    "        transaction_type=\"transfer\",\n",
    "        account_from=\"abc\",\n",
    "        account_to=\"xyz\"\n",
    "    )\n",
    "except Exception as e:\n",
    "    print(\"Invalid Account Format Test Passed:\", e)\n",
    "\n",
    "# Test 5: Transfer to Same Account\n",
    "try:\n",
    "    Transaction(\n",
    "        transaction_id=\"TXN005\",\n",
    "        amount=100,\n",
    "        timestamp=datetime.now(),\n",
    "        transaction_type=\"transfer\",\n",
    "        account_from=\"1234567890\",\n",
    "        account_to=\"1234567890\"\n",
    "    )\n",
    "except Exception as e:\n",
    "    print(\"Same Account Transfer Test Passed:\", e)\n",
    "\n",
    "# Test 6: Over Max Limit (Audit Log Trigger)\n",
    "try:\n",
    "    over_limit_tx = Transaction(\n",
    "        transaction_id=\"TXN006\",\n",
    "        amount=6000,\n",
    "        timestamp=datetime.now(),\n",
    "        transaction_type=\"withdrawal\",\n",
    "        account_from=\"1234567890\",\n",
    "        account_to=None\n",
    "    )\n",
    "    print(\"Over Limit Transaction:\", over_limit_tx)\n",
    "    if over_limit_tx.amount > SecurityPolicy.MAX_TRANSACTION_LIMIT:\n",
    "        log_event(f\"Policy violation: transaction exceeded limit (${over_limit_tx.amount})\", level=\"warning\")\n",
    "except Exception as e:\n",
    "    print(\"Over Limit Test Failed:\", e)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "46957dae-ce95-4b7f-8559-c66ff6cb0bd9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Current Working Directory: C:\\Users\\kiboz\\OneDrive\\Secure-Banking-System\\SecureBankingProject\\tests\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "print(\"Current Working Directory:\", os.getcwd())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "ec33f845-f4b4-4b4a-b6c1-3886176a5289",
   "metadata": {},
   "outputs": [],
   "source": [
    "from transaction import Transaction\n",
    "from policy import SecurityPolicy\n",
    "from audit_log import log_event"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9641524e-24b7-4bf0-a215-8057f210fb4e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d739fd6f-2068-44a3-bebb-af379ba1f205",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
