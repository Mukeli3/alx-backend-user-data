#!/usr/bin/env python3
"""
Basic auth
"""
import base64
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Basic authentication class
    """
    def extract_base64_authorization_header(self, authorization_header:
                                            str) -> str:
        """
        returns the Authorization header Base64 part for a
        Basic Authentication
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ", 1)[1]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
        returns the decoded value of a Base64 str
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header, validate=True)
            return decoded.decode('utf-8')
        except Exception:
            return None
