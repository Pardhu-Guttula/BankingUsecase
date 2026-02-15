# Epic Title: Interaction History and Documentation Upload

from dashboard.models.interaction_history_model import InteractionHistory
from backend.app import db

class InteractionHistoryRepository:
    @staticmethod
    def save(interaction: InteractionHistory) -> None:
        db.session.add(interaction)
        db.session.commit()

    @staticmethod
    def get_interactions_by_user_id(user_id: int) -> list[InteractionHistory]:
        return InteractionHistory.query.filter_by(user_id=user_id).order_by(InteractionHistory.timestamp.desc()).all()


# File 3: Interaction History Service for Business Logic in dashboard/services/interaction_history_service.py