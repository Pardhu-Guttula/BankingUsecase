# Epic Title: User Authentication and Security

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.app import db

class UserAuthentication(db.Model):
    __tablename__ = 'user_authentications'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    password_hash = Column(String(255), nullable=False)
    mfa_secret = Column(String(255), nullable=True)

    user = relationship('User', backref='user_authentications')

    def __init__(self, user_id: int, password_hash: str, mfa_secret: str = None):
        self.user_id = user_id
        self.password_hash = password_hash
        self.mfa_secret = mfa_secret

# File 2: User Authentication Repository in repositories/authentication/user_authentication_repository.py