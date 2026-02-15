# Epic Title: Personalized Dashboard

from backend.models.accounts.transaction_model import Transaction

class TransactionRepository:
    @staticmethod
    def find_by_account_id(account_id: int) -> list[Transaction]:
        return Transaction.query.filter_by(account_id=account_id).all()

    @staticmethod
    def save(transaction: Transaction) -> None:
        db.session.add(transaction)
        db.session.commit()


# File 6: Account Service to Handle Business Logic in services/accounts/account_service.py