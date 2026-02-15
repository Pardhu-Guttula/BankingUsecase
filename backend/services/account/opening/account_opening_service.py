# Epic Title: Account Opening and Service Modifications

from backend.repositories.accounts.account_repository import AccountRepository
from backend.models.accounts.account_model import Account

class AccountOpeningService:
    @staticmethod
    def open_account(user_id: int, first_name: str, last_name: str, email: str, age: int, initial_deposit: int) -> Account:
        account_number = AccountOpeningService.generate_account_number()
        account_type = "Standard"  # Placeholder, this could be determined through other logic
        account = AccountRepository.create_account(user_id, account_number, account_type, initial_deposit)
        return account

    @staticmethod
    def generate_account_number() -> str:
        # Logic to generate unique account number
        import uuid
        return str(uuid.uuid4()).replace('-', '')[:20]


# File 5: Controller to Handle Account Opening Requests in account/controllers/opening/account_opening_controller.py