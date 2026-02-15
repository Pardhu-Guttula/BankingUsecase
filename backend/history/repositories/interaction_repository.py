# Epic Title: Interaction History and Documentation Upload

from backend.models.interactions.interaction_model import Interaction
from backend.app import db

class InteractionRepository:
    @staticmethod
    def save(interaction: Interaction) -> None:
        db.session.add(interaction)
        db.session.commit()

    @staticmethod
    def get_interactions_by_user_id(user_id: int) -> list[Interaction]:
        return Interaction.query.filter_by(user_id=user_id).all()


# File 3: Interaction Service to Handle Business Logic for Interactions in history/services/interaction_service.py