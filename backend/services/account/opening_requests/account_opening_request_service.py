# Epic Title: Streamline Account Opening Requests

from backend.repositories.account.opening_requests.account_opening_request_repository import AccountOpeningRequestRepository
from backend.models.account.opening_requests.account_opening_request_model import AccountOpeningRequest

class AccountOpeningRequestService:
    @staticmethod
    def create_request(user_id: int, account_type: str) -> None:
        request = AccountOpeningRequest(user_id=user_id, account_type=account_type)
        AccountOpeningRequestRepository.save(request)

    @staticmethod
    def get_user_requests(user_id: int) -> list:
        return AccountOpeningRequestRepository.find_by_user_id(user_id)


# File 4: Account Opening Request Controller in controllers/account/opening_requests/account_opening_request_controller.py