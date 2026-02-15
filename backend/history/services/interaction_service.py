# Epic Title: Interaction History and Documentation Upload

from backend.models.interactions.interaction_model import Interaction
from backend.history.repositories.interaction_repository import InteractionRepository
from backend.app import db

class InteractionService:
    @staticmethod
    def log_interaction(user_id: int, action: string, details: str = None) -> bool:
        try:
            interaction = Interaction(user_id=user_id, action=action, details=details)
            InteractionRepository.save(interaction)
            return True
        except Exception as e:
            db.session.rollback()
            return False

    @staticmethod
    def get_user_interactions(user_id: int) -> list[Interaction]:
        return InteractionRepository.get_interactions_by_user_id(user_id)


# File 4: Interaction Controller to Expose Interaction Endpoints in history/controllers/interaction_controller.py