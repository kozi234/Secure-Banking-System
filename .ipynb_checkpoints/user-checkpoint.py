{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f753d296-fd0a-464e-b491-f37bdfa06bca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "models directory created: True\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "\n",
    "# Ensure the \"models\" directory exists\n",
    "os.makedirs(\"models\", exist_ok=True)\n",
    "\n",
    "# Verify that the directory exists\n",
    "print(\"models directory created:\", os.path.exists(\"models\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5575c9b7-edd6-45fc-9876-c2af20b92d48",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Writing models/user.py\n"
     ]
    }
   ],
   "source": [
    "%%writefile models/user.py\n",
    "from typing import Literal\n",
    "from pydantic import BaseModel, EmailStr, validator\n",
    "import re\n",
    "\n",
    "class User(BaseModel):\n",
    "    user_id: int\n",
    "    username: str\n",
    "    email: EmailStr\n",
    "    password_hash: str\n",
    "    role: Literal[\"customer\", \"admin\", \"teller\"]\n",
    "    is_active: bool\n",
    "\n",
    "    @validator(\"username\")\n",
    "    def validate_username(cls, value):\n",
    "        if not re.match(\"^[a-zA-Z0-9_]+$\", value):\n",
    "            raise ValueError(\"Username can only contain letters, numbers, and underscores.\")\n",
    "        if len(value) < 3 or len(value) > 20:\n",
    "            raise ValueError(\"Username must be between 3 and 20 characters long.\")\n",
    "        return value\n",
    "\n",
    "    @validator(\"password_hash\")\n",
    "    def check_password_strength(cls, value):\n",
    "        if len(value) < 60:  # Hash length check\n",
    "            raise ValueError(\"Invalid password hash format.\")\n",
    "        return value\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "84b40d2a-e252-41ce-b70d-8f6546059f05",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "user.py exists: True\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "\n",
    "# Check if the file exists\n",
    "print(\"user.py exists:\", os.path.exists(\"models/user.py\"))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a696ab2f-17e1-43dd-9af7-1a197a103350",
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
