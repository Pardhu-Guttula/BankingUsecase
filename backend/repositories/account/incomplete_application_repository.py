# Epic Title: Interaction History and Documentation Upload

from backend.models.account.incomplete_application_model import IncompleteApplication
from backend.app import db

class IncompleteApplicationRepository:
    @staticmethod
    def save(application: IncompleteApplication) -> None:
        db.session.add(application)
        db.session.commit()

    @staticmethod
    def get_by_user_id(user_id: int) -> list[IncompleteApplication]:
        return IncompleteApplication.query.filter_by(user_id=user_id).all()

# File 3: Incomplete Application Service in services/account/incomplete_application_service.py