# Epic Title: Manage Secure Storage of Credentials

from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
import os
import binascii

db = SQLAlchemy()

class Session(db.Model):
    __tablename__ = "sessions"
    
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    session_token: str = db.Column(db.String(255), unique=True, nullable=False)
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)
    last_activity: datetime = db.Column(db.DateTime, default=datetime.utcnow)
    
    def is_expired(self) -> bool:
        expiration_time = self.last_activity + timedelta(minutes=15)
        return datetime.utcnow() > expiration_time

    @staticmethod
    def generate_session_token() -> str:
        return binascii.hexlify(os.urandom(24)).decode()

    def __repr__(self) -> str:
        return f"<Session {self.session_token}>"