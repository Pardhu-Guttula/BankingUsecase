# Epic Title: Save and Resume Incomplete Applications

from backend.interaction_history.repositories.application_repository import ApplicationRepository
from backend.interaction_history.models.application_model import Application

class ApplicationService:
    @staticmethod
    def save_application(user_id: int, data: str) -> None:
        application = Application(user_id=user_id, data=data)
        ApplicationRepository.save_application(application)

    @staticmethod
    def resume_application(app_id: int) -> Application:
        return ApplicationRepository.get_application_by_id(app_id)

    @staticmethod
    def get_user_applications(user_id: int) -> list[Application]:
        return ApplicationRepository.get_applications_by_user(user_id)


# File 4: Application Controller for Handling Requests in interaction_history/controllers/application_controller.py