# Epic Title: Interaction History and Documentation Upload

from backend.repositories.interactions.interaction_repository import InteractionRepository
from backend.models.interactions.interaction_model import Interaction

class InteractionService:
    @staticmethod
    def log_interaction(user_id: int, action: str, description: str = None) -> Interaction:
        interaction = Interaction(user_id, action, description)
        InteractionRepository.save(interaction)
        return interaction

    @staticmethod
    def get_interaction_history(user_id: int) -> list[Interaction]:
        return InteractionRepository.find_by_user_id(user_id)


# File 5: Interaction Controller to Manage Interaction History in controllers/dashboard/interaction_controller.py