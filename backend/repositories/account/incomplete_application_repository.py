# Epic Title: Interaction History and Documentation Upload

from backend.models.account.incomplete_application_model import IncompleteApplication
from backend.app import db

class IncompleteApplicationRepository:
    @staticmethod
    def get_incomplete_applications_by_user(user_id: int) -> list[IncompleteApplication]:
        return IncompleteApplication.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_incomplete_application_by_id(application_id: int) -> IncompleteApplication:
        return IncompleteApplication.query.get(application_id)

    @staticmethod
    def save(application: IncompleteApplication) -> None:
        db.session.add(application)
        db.session.commit()

    @staticmethod
    def update(application: IncompleteApplication) -> None:
        db.session.commit()


# File 4: Incomplete Application Service Layer in services/account/incomplete_application_service.py