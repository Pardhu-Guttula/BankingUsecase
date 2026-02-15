# Epic Title: User Authentication and Security

from backend.models.authentication.two_factor_model import TwoFactorAuth
from backend.app import db

class TwoFactorAuthRepository:
    @staticmethod
    def get_by_user_id(user_id: int) -> TwoFactorAuth:
        return TwoFactorAuth.query.filter_by(user_id=user_id).first()

    @staticmethod
    def save(two_factor: TwoFactorAuth) -> None:
        db.session.add(two_factor)
        db.session.commit()


# File 5: Authentication Service Implementing Login Logic in authentication/services/authentication_service.py