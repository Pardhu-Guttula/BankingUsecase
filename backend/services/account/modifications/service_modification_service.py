# Epic Title: Account Opening and Service Modifications

from backend.models.account.modifications.service_modification_model import ServiceModification
from backend.repositories.account.modifications.service_modification_repository import ServiceModificationRepository

class ServiceModificationService:
    @staticmethod
    def submit_service_modification(user_id: int, service_type: str) -> ServiceModification:
        service_modification = ServiceModification(user_id=user_id, service_type=service_type)
        ServiceModificationRepository.save(service_modification)
        return service_modification

    @staticmethod
    def get_user_service_modifications(user_id: int) -> list[ServiceModification]:
        return ServiceModificationRepository.get_by_user_id(user_id)

# File 4: Service Modification Controller in controllers/account/modifications/service_modification_controller.py