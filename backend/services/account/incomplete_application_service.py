# Epic Title: Interaction History and Documentation Upload

from backend.models.account.incomplete_application_model import IncompleteApplication
from backend.repositories.account.incomplete_application_repository import IncompleteApplicationRepository

class IncompleteApplicationService:
    @staticmethod
    def save_application(user_id: int, form_data: str) -> IncompleteApplication:
        application = IncompleteApplication(user_id=user_id, form_data=form_data)
        IncompleteApplicationRepository.save(application)
        return application

    @staticmethod
    def get_user_applications(user_id: int) -> list[IncompleteApplication]:
        return IncompleteApplicationRepository.get_by_user_id(user_id)

# File 4: Incomplete Application Controller in controllers/account/incomplete_application_controller.py