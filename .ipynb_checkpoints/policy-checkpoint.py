{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bcef3aa7-00f3-4989-beb4-dad9e0cba3d1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Writing models/policy.py\n"
     ]
    }
   ],
   "source": [
    "%%writefile models/policy.py\n",
    "class SecurityPolicy:\n",
    "    MIN_PASSWORD_LENGTH = 10\n",
    "    PASSWORD_COMPLEXITY_REGEX = r\"^(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*#?&])[A-Za-z\\d@$!%*#?&]{10,}$\"\n",
    "    MAX_TRANSACTION_LIMIT = 5000.00"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4c8fee1b-a956-4057-ab2b-5f76d3870d73",
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
