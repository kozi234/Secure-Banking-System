{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cead5294-72fc-48e5-b674-c092668eea5f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys\n",
    "import os\n",
    "\n",
    "# Get the absolute path of the project root directory\n",
    "sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), \"..\")))\n",
    "\n",
    "from models.user import User  # Import the User model\n",
    "\n",
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
    "        )\n"
   ]
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
