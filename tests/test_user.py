import sys
import os
import pytest
import bcrypt
from models.user import User

# Get the absolute path of the project root directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Function to hash passwords for testing
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def test_valid_user():
    user = User(
        user_id=1,
        username="JohnDoe_92",
        email="johndoe@example.com",
        password_hash=hash_password("SecurePassword123!"),  # Properly hashed
        role="customer",
        is_active=True
    )
    assert user.username == "JohnDoe_92"

def test_invalid_username():
    with pytest.raises(ValueError):
        User(
            user_id=2,
            username="*baduser!",
            email="baduser@example.com",
            password_hash=hash_password("SecurePassword123!"),
            role="customer",
            is_active=True
        )

def test_invalid_password_hash():
    with pytest.raises(ValueError):
        User(
            user_id=3,
            username="secureuser",
            email="secure@example.com",
            password_hash="not_a_real_hash",  # Invalid hash format
            role="admin",
            is_active=True
        )
