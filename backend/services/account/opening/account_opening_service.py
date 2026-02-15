# Epic Title: Account Opening and Service Modifications

from backend.repositories.accounts.account_repository import AccountRepository
from backend.models.accounts.account_model import Account
from backend.services.approval_workflow.approval_service import ApprovalService

class AccountOpeningService:
    @staticmethod
    def open_account(user_id: int, first_name: str, last_name: str, email: str, age: int, initial_deposit: int) -> Account:
        account_number = AccountOpeningService.generate_account_number()
        account_type = "Standard"  # Placeholder, this could be determined through other logic
        account = AccountRepository.create_account(user_id, account_number, account_type, initial_deposit)

        # Submit account opening request for approval
        ApprovalService.submit_for_approval(account.id, "Account Opening")

        return account

    @staticmethod
    def generate_account_number() -> str:
        # Logic to generate unique account number
        import uuid
        return str(uuid.uuid4()).replace('-', '')[:20]
    

# File 7: Controller Integration for Account Opening in controllers/account/controllers/opening/account_opening_controller.py (Update)