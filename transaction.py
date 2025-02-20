{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f365132d-8c39-4c6f-bba0-da3337e34c24",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Writing models/transaction.py\n"
     ]
    }
   ],
   "source": [
    "%%writefile models/transaction.py\n",
    "from datetime import datetime\n",
    "from pydantic import BaseModel, validator\n",
    "from typing import Literal\n",
    "\n",
    "class Transaction(BaseModel):\n",
    "    transaction_id: str\n",
    "    amount: float\n",
    "    timestamp: datetime\n",
    "    transaction_type: Literal[\"deposit\", \"withdrawal\", \"transfer\"]\n",
    "    account_from: str\n",
    "    account_to: str\n",
    "\n",
    "    @validator(\"amount\")\n",
    "    def validate_amount(cls, value):\n",
    "        if value <= 0:\n",
    "            raise ValueError(\"Transaction amount must be greater than 0.\")\n",
    "        return round(value, 2)\n",
    "\n",
    "    @validator(\"account_from\", \"account_to\")\n",
    "    def validate_accounts(cls, value):\n",
    "        if len(value) != 10:\n",
    "            raise ValueError(\"Invalid account format. Must be 10 alphanumeric characters.\")\n",
    "        return value\n",
    "\n",
    "    @validator(\"account_to\")\n",
    "    def check_transfer_accounts(cls, value, values):\n",
    "        if \"account_from\" in values and value == values[\"account_from\"]:\n",
    "            raise ValueError(\"Cannot transfer to the same account.\")\n",
    "        return value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "658d42fa-7de0-453d-aae7-be4ab471f19e",
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
