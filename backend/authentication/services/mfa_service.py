# Epic Title: User Authentication and Security

import pyotp
import logging
from flask_sqlalchemy import SQLAlchemy
from backend.authentication.models import User

logger = logging.getLogger(__name__)

class MFAService:
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def generate_totp_secret(self) -> str:
        return pyotp.random_base32()

    def validate_totp(self, user: User, token: str) -> bool:
        if not user.mfa_secret:
            return False
        totp = pyotp.TOTP(user.mfa_secret)
        return totp.verify(token)

    def setup_totp(self, user: User) -> str:
        secret = self.generate_totp_secret()
        user.enable_mfa(secret)
        self.db.session.commit()
        logger.info(f"MFA setup completed for user {user.id}")
        return secret

    def disable_totp(self, user: User):
        user.disable_mfa()
        self.db.session.commit()
        logger.info(f"MFA disabled for user {user.id}")