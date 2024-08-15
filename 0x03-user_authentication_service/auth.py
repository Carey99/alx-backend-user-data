from db import DB
from user import User
import bcrypt


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """returns a salted hash of the input"""
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def register_user(self, email: str, password: str) -> User:
        """Register a new user with email and password"""
        try:
            # Check if user already exists
            existing_user = self._db.find_user_by(email=email)
            if existing_user:
                raise ValueError(f"User {email} already exists")
        except Exception:
            # If user does not exist, proceed to create a new user
            hashed_password = self._hash_password(password)
            new_user = self._db.add_user(email=email,
                                         hashed_password=hashed_password)
            return new_user
        # If user already exists, raise a ValueError
        raise ValueError(f"User {email} already exists")
