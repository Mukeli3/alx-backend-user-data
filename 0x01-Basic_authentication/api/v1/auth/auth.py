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
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        path = path if path.endswith('/') else path + '/'
        for excluded_path in excluded_paths:
            if path == excluded_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        authorization header from the request
        """
        if request is None:
            return None
        return request.headers.get('Authorization') or None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current user from request
        """
        return None
