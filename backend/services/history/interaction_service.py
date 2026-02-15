# Epic Title: Maintain Interaction History

from backend.repositories.history.interaction_repository import InteractionRepository
from backend.models.history.interaction_model import Interaction

class InteractionService:

    @staticmethod
    def create_interaction(user_id: int, action: str) -> None:
        interaction = Interaction(user_id=user_id, action=action)
        InteractionRepository.save(interaction)

    @staticmethod
    def get_interactions_by_user(user_id: int) -> list[Interaction]:
        return InteractionRepository.find_by_user_id(user_id)


# File 4: Interaction History Controller in `controllers/history/interaction_controller.py`