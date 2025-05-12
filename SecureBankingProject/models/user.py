"""
Title: User Model for Secure Banking System
Author: John A. Kibozi
Course: CSC3028X00
Date: March 10, 2025
Description:
This module defines the User model using Pydantic for validation.
Includes:
- Username validation
- Email format validation
- Secure password hashing and verification using bcrypt
"""

from typing import Literal
from pydantic import BaseModel, EmailStr, field_validator
import re
import bcrypt
from models.policy import SecurityPolicy  # If policy.py is inside the 'models' folder

class User(BaseModel):
    user_id: int
    username: str
    email: EmailStr
    password_hash: str
    role: Literal["customer", "admin", "teller"]
    is_active: bool

    @field_validator("username")
    @classmethod
    def validate_username(cls, value):
        """Ensure the username follows proper format."""
        if not re.match("^[a-zA-Z0-9_]+$", value):
            raise ValueError("Username can only contain letters, numbers, and underscores.")
        if len(value) < 3 or len(value) > 20:
            raise ValueError("Username must be between 3 and 20 characters long.")
        return value

    @staticmethod
    def hash_password(password: str) -> str:
        """Hash password using bcrypt if it meets SecurityPolicy standards."""
        if not re.match(SecurityPolicy.PASSWORD_COMPLEXITY_REGEX, password):
            raise ValueError("Password does not meet security complexity requirements.")

        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt).decode()

    @classmethod
    def create_user(cls, user_id: int, username: str, email: str, password: str, role: str):
        """Creates a user with a hashed password after validation."""
        hashed_password = cls.hash_password(password)
        return cls(user_id=user_id, username=username, email=email, password_hash=hashed_password, role=role, is_active=True)

    @field_validator("password_hash")
    @classmethod
    def check_password_hash(cls, value):
        """Ensure the password is properly hashed using bcrypt."""
        try:
            if not value.startswith("$2b$") and not value.startswith("$2a$"):
                raise ValueError("Password hash format is invalid.")
            bcrypt.checkpw("test_password".encode(), value.encode())  # Check if it's a valid bcrypt hash
        except ValueError:
            raise ValueError("Invalid password hash format.")
        except Exception:
            raise ValueError("Hash verification failed.")
        return value

# Standalone functions for password hashing & verification
def hash_password(plain_text_password: str) -> str:
    """Hashes a plaintext password using bcrypt."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(plain_text_password.encode(), salt)
    return hashed_password.decode()

def verify_password(plain_text_password: str, hashed_password: str) -> bool:
    """Verifies a plaintext password against a stored hash."""
    return bcrypt.checkpw(plain_text_password.encode(), hashed_password.encode())

# Example usage:
if __name__ == "__main__":
    # Example user creation
    plain_password = "SecurePass123"
    hashed_pw = hash_password(plain_password)
    print(f"Plain Password: {plain_password}")
    print(f"Hashed Password: {hashed_pw}")

    # Verify password
    is_valid = verify_password(plain_password, hashed_pw)
    print(f"Password Match: {is_valid}")