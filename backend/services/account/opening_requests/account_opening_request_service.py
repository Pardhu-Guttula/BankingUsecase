# Epic Title: Account Opening and Service Modifications

from backend.models.account.opening_requests.account_opening_request_model import AccountOpeningRequest
from backend.repositories.account.opening_requests.account_opening_request_repository import AccountOpeningRequestRepository

class AccountOpeningRequestService:
    @staticmethod
    def create_request(user_id: int, account_type: str) -> AccountOpeningRequest:
        request = AccountOpeningRequest(user_id=user_id, account_type=account_type)
        AccountOpeningRequestRepository.save(request)
        return request

    @staticmethod
    def get_user_requests(user_id: int) -> list[AccountOpeningRequest]:
        return AccountOpeningRequestRepository.get_by_user_id(user_id)

# File 4: Account Opening Request Controller in controllers/account/opening_requests/account_opening_request_controller.py