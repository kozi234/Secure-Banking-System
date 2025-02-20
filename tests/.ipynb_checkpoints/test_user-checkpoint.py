import sys
import os

# Get the absolute path of the project root directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.user import User  # Import the User model

import pytest
from models.user import User

def test_valid_user():
    user = User(
        user_id=1,
        username="JohnDoe_92",
        email="johndoe@example.com",
        password_hash="hashed_password_string_that_is_correct_length",
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
            password_hash="hashed_password",
            role="customer",
            is_active=True
        )

def test_invalid_password_hash():
    with pytest.raises(ValueError):
        User(
            user_id=3,
            username="secureuser",
            email="secure@example.com",
            password_hash="short_hash",
            role="admin",
            is_active=True
        )
