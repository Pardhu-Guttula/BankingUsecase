# Epic Title: Maintain Interaction History

from typing import List
from backend.interaction_history.models.interaction_model import Interaction
from backend.app import db

class InteractionRepository:
    @staticmethod
    def get_interactions_by_user(user_id: int) -> List[Interaction]:
        return Interaction.query.filter_by(user_id=user_id).all()

    @staticmethod
    def add_interaction(interaction: Interaction) -> None:
        db.session.add(interaction)
        db.session.commit()


# File 3: Interaction Service for Business Logic in interaction_history/services/interaction_service.py