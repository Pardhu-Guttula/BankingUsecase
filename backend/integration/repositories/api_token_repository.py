# Epic Title: Core Banking System Integration

from backend.models.core_banking.api_token_model import APIToken
from backend.app import db
import datetime

class APITokenRepository:
    @staticmethod
    def save(token: APIToken) -> None:
        db.session.add(token)
        db.session.commit()

    @staticmethod
    def get_valid_token(token: str) -> APIToken:
        return APIToken.query.filter_by(token=token).filter(APIToken.expires_at > datetime.datetime.utcnow()).first()

    @staticmethod
    def delete(token: APIToken) -> None:
        db.session.delete(token)
        db.session.commit()


# File 3: Secure API Service for Core Banking Integration in integration/services/api_service.py