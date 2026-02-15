# Epic Title: Core Banking System Integration

from backend.integration.repositories.api_token_repository import APITokenRepository
from backend.models.core_banking.api_token_model import APIToken
from flask import current_app
import datetime
import hashlib
import os

class APIService:
    @staticmethod
    def generate_token(expiration_minutes: int = 60) -> str:
        token = hashlib.sha256(os.urandom(64)).hexdigest()
        expires_at = datetime.datetime.utcnow() + datetime.timedelta(minutes=expiration_minutes)
        api_token = APIToken(token=token, expires_at=expires_at)
        APITokenRepository.save(api_token)
        return token

    @staticmethod
    def validate_token(token: str) -> bool:
        valid_token = APITokenRepository.get_valid_token(token)
        return valid_token is not None


# File 4: Core Banking API Controller to Expose Secure Endpoints in integration/controllers/api_controller.py