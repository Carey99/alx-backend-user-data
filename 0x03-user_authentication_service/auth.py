#!/usr/bin/env python3
"""
    takes a passwoord strinng and returns bytes
    the returned byte a salted hhashh of tthe input
    hasheddd with bcrypt
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """returns a salted hash of the input"""
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def register_user(self, email: str, password: str) -> User:
        """register a new user"""
        try:
            exists = self._db.find_user_by(email=email)
            if exists:
                raise ValueError(f"User {email} already exists")
        except Exception:
            password = self._hash_password(password)
            return self._db.add_user(email=email,
                                     hashed_password=password)
