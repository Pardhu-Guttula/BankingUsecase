# Epic Title: Interaction History and Documentation Upload

from backend.repositories.interactions.application_repository import ApplicationRepository
from backend.models.interactions.application_model import Application

class ApplicationService:
    @staticmethod
    def save_application(user_id: int, status: str, data: str = None) -> Application:
        application = Application(user_id, status, data)
        ApplicationRepository.save(application)
        return application

    @staticmethod
    def get_user_applications(user_id: int) -> list[Application]:
        return ApplicationRepository.find_by_user_id(user_id)

    @staticmethod
    def get_application_by_id(application_id: int) -> Application:
        return ApplicationRepository.find_by_id(application_id)


# File 5: Application Form to Capture Application Data in forms/application_form.py