# Epic Title: Save and Resume Incomplete Applications

from backend.models.applications.incomplete_application_model import IncompleteApplication
from backend.app import db

class IncompleteApplicationRepository:
    @staticmethod
    def save(incomplete_application: IncompleteApplication) -> None:
        db.session.add(incomplete_application)
        db.session.commit()

    @staticmethod
    def update(incomplete_application: IncompleteApplication) -> None:
        db.session.commit()

    @staticmethod
    def find_by_user_id(user_id: int) -> IncompleteApplication:
        return IncompleteApplication.query.filter_by(user_id=user_id).order_by(IncompleteApplication.saved_at.desc()).first()


# File 3: Incomplete Application Service in `services/applications/incomplete_application_service.py`