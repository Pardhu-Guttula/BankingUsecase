# Epic Title: Interaction History and Documentation Upload

from backend.models.accounts.incomplete_application_model import IncompleteApplication
from backend.account.repositories.incomplete_application_repository import IncompleteApplicationRepository
from backend.app import db

class IncompleteApplicationService:
    @staticmethod
    def save_application(user_id: int, application_data: str) -> bool:
        try:
            application = IncompleteApplication(user_id=user_id, application_data=application_data)
            IncompleteApplicationRepository.save(application)
            return True
        except Exception as e:
            db.session.rollback()
            return False

    @staticmethod
    def get_incomplete_application(user_id: int) -> IncompleteApplication:
        return IncompleteApplicationRepository.get_incomplete_application_by_user_id(user_id)

    @staticmethod
    def delete_application(application: IncompleteApplication) -> bool:
        try:
            IncompleteApplicationRepository.delete(application)
            return True
        except Exception as e:
            db.session.rollback()
            return False


# File 4: Application Controller to Expose Application Endpoints in account/controllers/application_controller.py