# Epic Title: Personalized Dashboard

from backend.repositories.accounts.account_repository import AccountRepository
from backend.repositories.accounts.transaction_repository import TransactionRepository
from backend.models.accounts.account_model import Account
from backend.models.accounts.transaction_model import Transaction

class AccountService:
    @staticmethod
    def get_user_accounts(user_id: int) -> list[Account]:
        return AccountRepository.find_by_user_id(user_id)

    @staticmethod
    def get_account_transactions(account_id: int) -> list[Transaction]:
        return TransactionRepository.find_by_account_id(account_id)

    @staticmethod
    def create_account(user_id: int, account_number: str, account_type: str, balance: float) -> Account:
        account = Account(user_id, account_number, account_type, balance)
        AccountRepository.save(account)
        return account

    @staticmethod
    def create_transaction(account_id: int, amount: float, transaction_type: str, description: str = None) -> Transaction:
        transaction = Transaction(account_id, amount, transaction_type, description)
        TransactionRepository.save(transaction)
        return transaction


# File 7: Dashboard Controller to Handle User Requests in controllers/dashboard/dashboard_controller.py