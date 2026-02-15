# Epic Title: Account Opening and Service Modifications

from backend.models.accounts.service_modification_model import ServiceModification
from backend.account.repositories.service_modification_repository import ServiceModificationRepository
from backend.app import db

class ServiceModificationService:
    @staticmethod
    def modify_service(user_id: int, service_type: str, description: str) -> bool:
        try:
            service_modification = ServiceModification(user_id=user_id, service_type=service_type, description=description)
            ServiceModificationRepository.save(service_modification)
            return True
        except Exception as e:
            db.session.rollback()
            return False

# File 7: Update Main App to Register Service Modification Controller in app.py