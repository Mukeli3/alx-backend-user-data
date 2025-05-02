#!/usr/bin/env python3
import bcrypt


def hash_password(password):
    password = b'password'
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())

    return hashed
