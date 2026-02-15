# Epic Title: Account Opening and Service Modifications

from backend.models.account.opening.account_opening_request_model import AccountOpeningRequest
from backend.repositories.account.opening.account_opening_request_repository import AccountOpeningRequestRepository

class AccountOpeningRequestService:
    @staticmethod
    def create_account_opening_request(user_id: int, account_type: str, initial_deposit: float) -> AccountOpeningRequest:
        account_opening_request = AccountOpeningRequest(user_id=user_id, account_type=account_type, initial_deposit=initial_deposit)
        AccountOpeningRequestRepository.save(account_opening_request)
        return account_opening_request

    @staticmethod
    def get_user_account_opening_requests(user_id: int) -> list[AccountOpeningRequest]:
        return AccountOpeningRequestRepository.get_requests_by_user(user_id)

    @staticmethod
    def get_account_opening_request_by_id(request_id: int) -> AccountOpeningRequest:
        return AccountOpeningRequestRepository.get_request_by_id(request_id)


# File 4: Account Opening Form with Validations in forms/account_opening_form.py