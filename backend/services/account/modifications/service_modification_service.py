# Epic Title: Account Opening and Service Modifications

from backend.repositories.account.service_modification_repository import ServiceModificationRepository
from backend.models.account.service_modification_model import ServiceModification
from datetime import datetime

class ServiceModificationService:
    @staticmethod
    def modify_service(user_id: int, service_name: str, action: str) -> ServiceModification:
        service_modification = ServiceModification(user_id=user_id, service_name=service_name, action=action)
        ServiceModificationRepository.save(service_modification)
        return service_modification

    @staticmethod
    def approve_modification(service_modification_id: int) -> None:
        service_modification = ServiceModification.query.get(service_modification_id)
        if service_modification:
            service_modification.status = 'Approved'
            service_modification.approval_date = datetime.utcnow()
            ServiceModificationRepository.update(service_modification)


# File 6: Controller to Handle Service Modification Requests in account/controllers/modifications/service_modification_controller.py