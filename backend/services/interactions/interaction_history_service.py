# Epic Title: Interaction History and Documentation Upload

from backend.models.interactions.interaction_history_model import InteractionHistory
from backend.repositories.interactions.interaction_history_repository import InteractionHistoryRepository

class InteractionHistoryService:
    @staticmethod
    def create_interaction(user_id: int, action: str) -> InteractionHistory:
        interaction = InteractionHistory(user_id=user_id, action=action)
        InteractionHistoryRepository.save(interaction)
        return interaction

    @staticmethod
    def get_user_interactions(user_id: int) -> list[InteractionHistory]:
        return InteractionHistoryRepository.get_by_user_id(user_id)

# File 4: Interaction History Controller in controllers/interactions/interaction_history_controller.py