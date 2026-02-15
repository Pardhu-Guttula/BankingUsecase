# Epic Title: Maintain Interaction History

from backend.models.history.interaction_model import Interaction
from backend.app import db

class InteractionRepository:
    
    @staticmethod
    def save(interaction: Interaction) -> None:
        db.session.add(interaction)
        db.session.commit()

    @staticmethod
    def find_by_user_id(user_id: int) -> list[Interaction]:
        return Interaction.query.filter_by(user_id=user_id).order_by(Interaction.timestamp.desc()).all()


# File 3: Interaction History Service in `services/history/interaction_service.py`