{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "59a0cb80-cb2a-46c7-a5af-5dcbf8b0c430",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Writing models/account.py\n"
     ]
    }
   ],
   "source": [
    "%%writefile models/account.py\n",
    "from typing import Literal\n",
    "from pydantic import BaseModel, validator\n",
    "\n",
    "class Account(BaseModel):\n",
    "    account_id: str\n",
    "    account_type: Literal[\"savings\", \"checking\", \"investment\"]\n",
    "    balance: float\n",
    "    owner_id: int\n",
    "\n",
    "    @validator(\"account_id\")\n",
    "    def validate_account_id(cls, value):\n",
    "        if not value.isalnum() or len(value) != 10:\n",
    "            raise ValueError(\"Account ID must be exactly 10 alphanumeric characters.\")\n",
    "        return value\n",
    "\n",
    "    @validator(\"balance\")\n",
    "    def validate_balance(cls, value):\n",
    "        if value < 0:\n",
    "            raise ValueError(\"Balance cannot be negative.\")\n",
    "        return round(value, 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "59447228-0eed-4f90-b0b4-0b3f2054e331",
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
