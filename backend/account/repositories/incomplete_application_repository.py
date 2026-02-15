# Epic Title: Interaction History and Documentation Upload

from backend.models.accounts.incomplete_application_model import IncompleteApplication
from backend.app import db

class IncompleteApplicationRepository:
    @staticmethod
    def save(application: IncompleteApplication) -> None:
        db.session.add(application)
        db.session.commit()

    @staticmethod
    def get_incomplete_application_by_user_id(user_id: int) -> IncompleteApplication:
        return IncompleteApplication.query.filter_by(user_id=user_id).first()

    @staticmethod
    def delete(application: IncompleteApplication) -> None:
        db.session.delete(application)
        db.session.commit()


# File 3: Incomplete Application Service to Handle Business Logic in account/services/incomplete_application_service.py