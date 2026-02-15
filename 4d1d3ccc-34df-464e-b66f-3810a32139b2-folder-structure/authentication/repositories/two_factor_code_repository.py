# Epic Title: Implement Secure Login Mechanism

from authentication.models.two_factor_code_model import TwoFactorCode
from backend.app import db
from datetime import datetime, timedelta

class TwoFactorCodeRepository:
    @staticmethod
    def save(two_factor_code: TwoFactorCode) -> None:
        db.session.add(two_factor_code)
        db.session.commit()

    @staticmethod
    def get_active_code(user_id: int) -> TwoFactorCode:
        expiration_time = datetime.utcnow() - timedelta(minutes=5)
        return TwoFactorCode.query.filter(TwoFactorCode.user_id == user_id, TwoFactorCode.created_at > expiration_time).first()

    @staticmethod
    def delete_code(two_factor_code: TwoFactorCode) -> None:
        db.session.delete(two_factor_code)
        db.session.commit()


# File 5: Two-Factor Authentication Service in authentication/services/two_factor_service.py