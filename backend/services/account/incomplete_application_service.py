# Epic Title: Interaction History and Documentation Upload

from backend.models.account.incomplete_application_model import IncompleteApplication
from backend.repositories.account.incomplete_application_repository import IncompleteApplicationRepository


class IncompleteApplicationService:
    @staticmethod
    def save_incomplete_application(user_id: int, application_data: str) -> IncompleteApplication:
        incomplete_application = IncompleteApplicationRepository.get_incomplete_application(user_id)
        if incomplete_application:
            incomplete_application.application_data = application_data
            IncompleteApplicationRepository.update(incomplete_application)
        else:
            incomplete_application = IncompleteApplication(user_id=user_id, application_data=application_data)
            IncompleteApplicationRepository.save(incomplete_application)
        return incomplete_application

    @staticmethod
    def get_incomplete_application(user_id: int) -> IncompleteApplication:
        return IncompleteApplicationRepository.get_incomplete_application(user_id)


# File 4: Incomplete Application Controller Endpoint in account/controllers/incomplete_application_controller.py