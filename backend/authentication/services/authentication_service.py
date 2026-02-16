# Epic Title: Implement Secure Login Mechanism

import logging
from flask import request
from werkzeug.security import check_password_hash
from backend.authentication.models.user import User
from backend.authentication.models.session import Session
from typing import Optional

logger = logging.getLogger(__name__)

class AuthenticationService:
    def __init__(self, db):
        self.db = db
    
    def authenticate_user(self, username: str, password: str) -> Optional[User]:
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            logger.info(f"Authentication successful for user: {username}")
            return user
        logger.warning(f"Authentication failed for user: {username}")
        return None
    
    def create_session(self, user_id: int) -> Session:
        session_token = self._generate_session_token()
        session = Session(user_id=user_id, session_token=session_token)
        self.db.session.add(session)
        self.db.session.commit()
        logger.info(f"Session created for user_id: {user_id}")
        return session
    
    def _generate_session_token(self) -> str:
        import uuid
        return str(uuid.uuid4())