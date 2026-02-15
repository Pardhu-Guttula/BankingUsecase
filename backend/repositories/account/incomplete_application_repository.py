# Epic Title: Interaction History and Documentation Upload

from backend.models.account.incomplete_application_model import IncompleteApplication
from backend.app import db

class IncompleteApplicationRepository:
    @staticmethod
    def save(application: IncompleteApplication) -> None:
        db.session.add(application)
        db.session.commit()

    @staticmethod
    def get_incomplete_application_by_user_id(user_id: int) -> list[IncompleteApplication]:
        return IncompleteApplication.query.filter_by(user_id=user_id).order_by(IncompleteApplication.saved_at.desc()).all()
    
    @staticmethod
    def get_incomplete_application_by_id(application_id: int) -> IncompleteApplication:
        return IncompleteApplication.query.filter_by(id=application_id).first()

# File 3: IncompleteApplication Service to Handle Business Logic in services/account/incomplete_application_service.py