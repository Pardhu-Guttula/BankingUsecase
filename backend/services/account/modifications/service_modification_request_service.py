# Epic Title: Account Opening and Service Modifications

from backend.models.account.modifications.service_modification_request_model import ServiceModificationRequest
from backend.repositories.account.modifications.service_modification_request_repository import ServiceModificationRequestRepository

class ServiceModificationRequestService:
    @staticmethod
    def create_request(user_id: int, account_id: int, service_type: str) -> ServiceModificationRequest:
        request = ServiceModificationRequest(user_id=user_id, account_id=account_id, service_type=service_type)
        ServiceModificationRequestRepository.save(request)
        return request

    @staticmethod
    def get_user_requests(user_id: int) -> list[ServiceModificationRequest]:
        return ServiceModificationRequestRepository.get_by_user_id(user_id)

    @staticmethod
    def get_account_requests(account_id: int) -> list[ServiceModificationRequest]:
        return ServiceModificationRequestRepository.get_by_account_id(account_id)

# File 4: Service Modification Request Controller in controllers/account/modifications/service_modification_request_controller.py