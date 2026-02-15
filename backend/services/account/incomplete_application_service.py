# Epic Title: Interaction History and Documentation Upload

from backend.models.account.incomplete_application_model import IncompleteApplication
from backend.repositories.account.incomplete_application_repository import IncompleteApplicationRepository

class IncompleteApplicationService:
    @staticmethod
    def save_incomplete_application(user_id: int, status: str, application_data: str) -> IncompleteApplication:
        incomplete_application = IncompleteApplication(user_id=user_id, status=status, application_data=application_data)
        IncompleteApplicationRepository.save(incomplete_application)
        return incomplete_application

    @staticmethod
    def get_incomplete_applications(user_id: int) -> list[IncompleteApplication]:
        return IncompleteApplicationRepository.get_incomplete_application_by_user_id(user_id)

    @staticmethod
    def get_incomplete_application_by_id(application_id: int) -> IncompleteApplication:
        return IncompleteApplicationRepository.get_incomplete_application_by_id(application_id)

# File 4: Incomplete Application Controller to Handle Save and Resume in account/controllers/incomplete_application_controller.py