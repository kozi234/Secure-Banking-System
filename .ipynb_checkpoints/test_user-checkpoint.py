{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "36fbf417-b471-401a-8ab4-dcd4e739ffb0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Writing tests/test_user.py\n"
     ]
    }
   ],
   "source": [
    "%%writefile tests/test_user.py\n",
    "import pytest\n",
    "from models.user import User\n",
    "\n",
    "def test_valid_user():\n",
    "    user = User(\n",
    "        user_id=1,\n",
    "        username=\"JohnDoe_92\",\n",
    "        email=\"johndoe@example.com\",\n",
    "        password_hash=\"hashed_password_string_that_is_correct_length\",\n",
    "        role=\"customer\",\n",
    "        is_active=True\n",
    "    )\n",
    "    assert user.username == \"JohnDoe_92\"\n",
    "\n",
    "def test_invalid_username():\n",
    "    with pytest.raises(ValueError):\n",
    "        User(\n",
    "            user_id=2,\n",
    "            username=\"*baduser!\",\n",
    "            email=\"baduser@example.com\",\n",
    "            password_hash=\"hashed_password\",\n",
    "            role=\"customer\",\n",
    "            is_active=True\n",
    "        )\n",
    "\n",
    "def test_invalid_password_hash():\n",
    "    with pytest.raises(ValueError):\n",
    "        User(\n",
    "            user_id=3,\n",
    "            username=\"secureuser\",\n",
    "            email=\"secure@example.com\",\n",
    "            password_hash=\"short_hash\",\n",
    "            role=\"admin\",\n",
    "            is_active=True\n",
    "        )\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "79ba763c-2f8b-4885-9285-7f9888eaf604",
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
