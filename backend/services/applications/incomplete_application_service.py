# Epic Title: Save and Resume Incomplete Applications

from backend.repositories.applications.incomplete_application_repository import IncompleteApplicationRepository
from backend.models.applications.incomplete_application_model import IncompleteApplication
from datetime import datetime

class IncompleteApplicationService:
    @staticmethod
    def save_application(user_id: int, application_data: str) -> None:
        incomplete_application = IncompleteApplication(user_id=user_id, application_data=application_data)
        IncompleteApplicationRepository.save(incomplete_application)

    @staticmethod
    def update_application(user_id: int, application_data: str) -> None:
        incomplete_application = IncompleteApplicationRepository.find_by_user_id(user_id)
        if incomplete_application:
            incomplete_application.application_data = application_data
            incomplete_application.saved_at = datetime.utcnow()
            IncompleteApplicationRepository.update(incomplete_application)

    @staticmethod
    def get_application(user_id: int) -> IncompleteApplication:
        return IncompleteApplicationRepository.find_by_user_id(user_id)


# File 4: Incomplete Application Controller in `controllers/applications/incomplete_application_controller.py`