from typing import Literal
from pydantic import BaseModel, EmailStr, field_validator
import re
import bcrypt

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
        if not re.match("^[a-zA-Z0-9_]+$", value):
            raise ValueError("Username can only contain letters, numbers, and underscores.")
        if len(value) < 3 or len(value) > 20:
            raise ValueError("Username must be between 3 and 20 characters long.")
        return value

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