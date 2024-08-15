#!/usr/bin/env python3
"""
    takes a passwoord strinng and returns bytes
    the returned byte a salted hhashh of tthe input
    hasheddd with bcrypt
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """returns a salted hash of the input"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
