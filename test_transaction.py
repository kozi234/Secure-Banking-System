{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1a58a51f-bd2d-4d29-8b1d-5d3c5f0f4e22",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Overwriting tests/test_transaction.py\n"
     ]
    }
   ],
   "source": [
    "%%writefile tests/test_transaction.py\n",
    "import pytest\n",
    "from datetime import datetime\n",
    "from models.transaction import Transaction\n",
    "\n",
    "def test_valid_transaction():\n",
    "    transaction = Transaction(\n",
    "        transaction_id=\"txn123\",\n",
    "        amount=250.99,\n",
    "        timestamp=datetime.now(),\n",
    "        transaction_type=\"deposit\",\n",
    "        account_from=\"123456789A\",\n",
    "        account_to=\"987654321B\"\n",
    "    )\n",
    "    assert transaction.amount == 250.99\n",
    "\n",
    "def test_invalid_transfer():\n",
    "    with pytest.raises(ValueError):\n",
    "        Transaction(\n",
    "            transaction_id=\"txn456\",\n",
    "            amount=100.00,\n",
    "            timestamp=datetime.now(),\n",
    "            transaction_type=\"transfer\",\n",
    "            account_from=\"123456789A\",\n",
    "            account_to=\"123456789A\"\n",
    "        )\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5e620131-ac86-40b8-ac07-01259f3941ca",
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
