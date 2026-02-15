# Epic Title: Interaction History and Documentation Upload

from backend.models.interactions.interaction_history_model import InteractionHistory
from backend.app import db

class InteractionHistoryRepository:
    @staticmethod
    def get_history_by_user(user_id: int) -> list[InteractionHistory]:
        return InteractionHistory.query.filter_by(user_id=user_id).all()

    @staticmethod
    def save(interaction: InteractionHistory) -> None:
        db.session.add(interaction)
        db.session.commit()


# File 4: Interaction History Service Layer in services/interactions/interaction_history_service.py