#!/usr/bin/env python3
"""
authentication template
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    manage the API authentication (template)
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        check if authentication is required for a
        given path
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        authorization header from the request
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current user from request
        """
        return None
