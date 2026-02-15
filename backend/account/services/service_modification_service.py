# Epic Title: Account Opening and Service Modifications

from backend.models.accounts.service_modification_request import ServiceModificationRequest
from backend.account.repositories.service_modification_repository import ServiceModificationRepository
from backend.app import db

class ServiceModificationService:
    @staticmethod
    def modify_service(user_id: int, service_name: str, modification_type: str, reason: str) -> bool:
        try:
            modification_request = ServiceModificationRequest(user_id=user_id, service_name=service_name, modification_type=modification_type, reason=reason, status='pending')
            ServiceModificationRepository.save(modification_request)
            return True
        except Exception as e:
            db.session.rollback()
            return False


# File 4: Service Modification Repository to Manage Requests in account/repositories/service_modification_repository.py