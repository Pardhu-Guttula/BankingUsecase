# Epic Title: Account Opening and Service Modifications

from backend.models.account.opening.account_opening_model import AccountOpening
from backend.app import db

class AccountOpeningRepository:
    @staticmethod
    def save(account_opening: AccountOpening) -> None:
        db.session.add(account_opening)
        db.session.commit()

    @staticmethod
    def get_by_user_id(user_id: int) -> list[AccountOpening]:
        return AccountOpening.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_by_id(account_opening_id: int) -> AccountOpening:
        return AccountOpening.query.filter_by(id=account_opening_id).first()

    @staticmethod
    def update_status(account_opening_id: int, status: str) -> None:
        account_opening = AccountOpeningRepository.get_by_id(account_opening_id)
        if account_opening:
            account_opening.status = status
            db.session.commit()

# File 3: Account Opening Service in services/account/opening/account_opening_service.py