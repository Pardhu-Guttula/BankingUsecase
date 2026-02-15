# Epic Title: Interaction History and Documentation Upload

from backend.models.interactions.application_model import Application

class ApplicationRepository:
    @staticmethod
    def save(application: Application) -> None:
        db.session.add(application)
        db.session.commit()

    @staticmethod
    def find_by_user_id(user_id: int) -> list[Application]:
        return Application.query.filter_by(user_id=user_id).all()

    @staticmethod
    def find_by_id(application_id: int) -> Application:
        return Application.query.get(application_id)


# File 4: Application Service to Handle Business Logic in services/interactions/application_service.py