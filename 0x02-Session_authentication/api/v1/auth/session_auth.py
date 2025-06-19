#!/usr/bin/env python3
"""
session authentication
"""
import uuid
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """
    Session Authentication
    """
    user_id_by_session_id = {}  # class attribute

    def create_session(self, user_id: str = None) -> str:
        """
        creates a session id for a user id
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        # map session ID to user ID
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id
