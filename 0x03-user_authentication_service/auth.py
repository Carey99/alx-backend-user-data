#!/usr/bin/env python3
"""
    takes a passwoord strinng and returns bytes
    the returned byte a salted hhashh of tthe input
    hasheddd with bcrypt
"""
import bcrypt
from db import DB, NoResultFound
from user import User


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
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            return self._db.add_user(email, self._hash_password(password))
