# Epic Title: Maintain Interaction History

from typing import List
from backend.interaction_history.repositories.interaction_repository import InteractionRepository
from backend.interaction_history.models.interaction_model import Interaction

class InteractionService:
    @staticmethod
    def get_user_interactions(user_id: int) -> List[Interaction]:
        return InteractionRepository.get_interactions_by_user(user_id)

    @staticmethod
    def record_interaction(user_id: int, action: str) -> None:
        interaction = Interaction(user_id=user_id, action=action)
        InteractionRepository.add_interaction(interaction)


# File 4: Interaction Controller for Handling Requests in interaction_history/controllers/interaction_controller.py