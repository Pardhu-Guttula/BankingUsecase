# Epic Title: User Authentication and Security

from backend.models.authentication.mfa_model import MFA
from backend.app import db


class MFARepository:
    @staticmethod
    def save(mfa: MFA) -> None:
        db.session.add(mfa)
        db.session.commit()

    @staticmethod
    def get_mfa_by_user_id(user_id: int) -> MFA:
        return MFA.query.filter_by(user_id=user_id).first()

    @staticmethod
    def update(mfa: MFA) -> None:
        db.session.commit()


# File 3: MFA Service to Handle Business Logic in services/authentication/mfa_service.py