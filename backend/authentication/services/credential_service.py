# Epic Title: User Authentication and Security

import bcrypt
import logging

logger = logging.getLogger(__name__)

class CredentialService:
    def hash_password(self, password: str) -> str:
        # Generate a salt and hash the password
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        logger.debug(f"Password hashed.")
        return hashed.decode('utf-8')

    def check_password(self, hashed_password: str, password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))