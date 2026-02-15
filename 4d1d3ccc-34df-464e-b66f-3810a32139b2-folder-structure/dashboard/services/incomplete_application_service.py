# Epic Title: Interaction History and Documentation Upload

from dashboard.repositories.incomplete_application_repository import IncompleteApplicationRepository
from dashboard.models.incomplete_application_model import IncompleteApplication

class IncompleteApplicationService:
    @staticmethod
    def save_incomplete_application(user_id: int, application_data: str) -> IncompleteApplication:
        existing_application = IncompleteApplicationRepository.get_application_by_user_id(user_id)
        if existing_application:
            IncompleteApplicationRepository.delete(existing_application)
        incomplete_application = IncompleteApplication(user_id, application_data)
        IncompleteApplicationRepository.save(incomplete_application)
        return incomplete_application

    @staticmethod
    def get_incomplete_application(user_id: int) -> dict:
        application = IncompleteApplicationRepository.get_application_by_user_id(user_id)
        if application:
            return {
                "id": application.id,
                "application_data": application.application_data,
                "saved_at": application.saved_at
            }
        return {}


# File 4: Incomplete Application Controller for Handling Requests in dashboard/controllers/incomplete_application_controller.py