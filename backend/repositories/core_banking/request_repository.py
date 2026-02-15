# Epic Title: Core Banking System Integration

from backend.models.core_banking.request_model import Request
from backend.app import db

class RequestRepository:
    @staticmethod
    def save(request: Request) -> None:
        db.session.add(request)
        db.session.commit()

    @staticmethod
    def get_by_user_id(user_id: int) -> list[Request]:
        return Request.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_by_external_id(external_id: str) -> Request | None:
        return Request.query.filter_by(external_id=external_id).first()

# File 7: Register Core Banking Sync Controller Blueprint in app.py (Already Exists, Modified)