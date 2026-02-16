# Epic Title: Manage Secure Storage of Credentials

import logging
from datetime import datetime
from flask import request
from werkzeug.security import generate_password_hash
from backend.authentication.models.user import User
from backend.authentication.models.session import Session
from typing import Optional

logger = logging.getLogger(__name__)

class AuthenticationService:
    def __init__(self, db):
        self.db = db
    
    def authenticate_user(self, username: str, password: str) -> Optional[User]:
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            logger.info(f"Authentication successful for user: {username}")
            return user
        logger.warning(f"Authentication failed for user: {username}")
        return None
    
    def create_session(self, user_id: int) -> Session:
        session_token = Session.generate_session_token()
        session = Session(user_id=user_id, session_token=session_token)
        self.db.session.add(session)
        self.db.session.commit()
        logger.info(f"Session created for user_id: {user_id}")
        return session
    
    def update_last_activity(self, session_token: str):
        session = Session.query.filter_by(session_token=session_token).first()
        if session and not session.is_expired():
            session.last_activity = datetime.utcnow()
            self.db.session.commit()
            logger.info(f"Session updated for session_token: {session_token}")
    
    def is_session_valid(self, session_token: str) -> bool:
        session = Session.query.filter_by(session_token=session_token).first()
        if not session or session.is_expired():
            logger.info(f"Session expired or invalid: {session_token}")
            return False
        logger.info(f"Session valid: {session_token}")
        return True