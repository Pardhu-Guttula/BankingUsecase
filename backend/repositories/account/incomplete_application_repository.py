# Epic Title: Interaction History and Documentation Upload

from backend.models.account.incomplete_application_model import IncompleteApplication
from backend.app import db


class IncompleteApplicationRepository:
    @staticmethod
    def save(incomplete_application: IncompleteApplication) -> None:
        db.session.add(incomplete_application)
        db.session.commit()

    @staticmethod
    def get_incomplete_application(user_id: int) -> IncompleteApplication:
        return IncompleteApplication.query.filter_by(user_id=user_id).first()

    @staticmethod
    def update(incomplete_application: IncompleteApplication) -> None:
        db.session.commit()


# File 3: Incomplete Application Service to Handle Business Logic in services/account/incomplete_application_service.py