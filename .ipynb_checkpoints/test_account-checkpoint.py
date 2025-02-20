{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "dc4e6f07-1223-45a8-8c46-f627897073b9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Writing tests/test_account.py\n"
     ]
    }
   ],
   "source": [
    "%%writefile tests/test_account.py\n",
    "import pytest\n",
    "from models.account import Account\n",
    "\n",
    "def test_valid_account():\n",
    "    account = Account(\n",
    "        account_id=\"123456789A\",\n",
    "        account_type=\"savings\",\n",
    "        balance=500.75,\n",
    "        owner_id=1\n",
    "    )\n",
    "    assert account.balance == 500.75\n",
    "\n",
    "def test_invalid_account_id():\n",
    "    with pytest.raises(ValueError):\n",
    "        Account(\n",
    "            account_id=\"1234\",\n",
    "            account_type=\"savings\",\n",
    "            balance=500.75,\n",
    "            owner_id=1\n",
    "        )\n",
    "\n",
    "def test_negative_balance():\n",
    "    with pytest.raises(ValueError):\n",
    "        Account(\n",
    "            account_id=\"987654321B\",\n",
    "            account_type=\"checking\",\n",
    "            balance=-100.00,\n",
    "            owner_id=2\n",
    "        )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c9a09c4e-6b0a-49de-b66e-e3fb43557b6d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
