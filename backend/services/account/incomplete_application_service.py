# Epic Title: Interaction History and Documentation Upload

from backend.repositories.account.incomplete_application_repository import IncompleteApplicationRepository
from backend.models.account.incomplete_application_model import IncompleteApplication

class IncompleteApplicationService:
    @staticmethod
    def save_application(user_id: int, data: str) -> IncompleteApplication:
        application = IncompleteApplication(user_id=user_id, data=data)
        IncompleteApplicationRepository.save(application)
        return application

    @staticmethod
    def update_application(application_id: int, data: str) -> IncompleteApplication:
        application = IncompleteApplicationRepository.get_incomplete_application_by_id(application_id)
        if application:
            application.data = data
            IncompleteApplicationRepository.update(application)
        return application

    @staticmethod
    def get_user_applications(user_id: int) -> list[IncompleteApplication]:
        return IncompleteApplicationRepository.get_incomplete_applications_by_user(user_id)

    @staticmethod
    def get_application_by_id(application_id: int) -> IncompleteApplication:
        return IncompleteApplicationRepository.get_incomplete_application_by_id(application_id)


# File 5: Controller to Handle Incomplete Applications in account/controllers/incomplete_application_controller.py