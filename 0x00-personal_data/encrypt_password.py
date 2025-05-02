#!/usr/bin/env python3
"""
module defines hash_password function
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
     expects one string argument name password and returns
     a salted, hashed password, which is a byte string.
    """
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    return hashed
