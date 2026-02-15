# Epic Title: Account Opening and Service Modifications

from backend.models.accounts.account_model import Account
from backend.account.repositories.account_repository import AccountRepository
from backend.repositories.approval_workflow.approval_repository import ApprovalRepository
from backend.app import db

class AccountService:
    @staticmethod
    def open_account(user_id: int, full_name: str, email: str, initial_deposit: float, account_type: str) -> bool:
        try:
            account = Account(user_id=user_id, account_number=AccountService.generate_account_number(), account_type=account_type, balance=initial_deposit)
            AccountRepository.save(account)
            return True
        except Exception as e:
            db.session.rollback()
            return False

    @staticmethod
    def generate_account_number() -> str:
        # Assuming an account number is a unique 10-digit number
        import random
        return str(random.randint(1000000000, 9999999999))
    
    @staticmethod
    def approve_account_opening(request_id: int) -> bool:
        request = ApprovalRepository.find_by_id(request_id)
        if request and request.request_type == 'account_opening':
            # Logic to open account
            # For example, let's assume we create an Account here
            account = Account(user_id=request.user_id, account_number=AccountService.generate_account_number(), account_type='savings', balance=0.00)
            AccountRepository.save(account)
            request.status = 'approved'
            db.session.commit()
            return True
        return False


# File 6: Update Main App to Include Approval Workflow Controller in app.py