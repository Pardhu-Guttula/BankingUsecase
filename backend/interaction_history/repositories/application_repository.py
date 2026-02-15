# Epic Title: Save and Resume Incomplete Applications

from backend.interaction_history.models.application_model import Application
from backend.app import db

class ApplicationRepository:
    @staticmethod
    def save_application(app: Application) -> None:
        db.session.add(app)
        db.session.commit()

    @staticmethod
    def get_application_by_id(app_id: int) -> Application:
        return Application.query.get(app_id)

    @staticmethod
    def get_applications_by_user(user_id: int) -> list[Application]:
        return Application.query.filter_by(user_id=user_id, status='incomplete').all()


# File 3: Application Service for Business Logic in interaction_history/services/application_service.py