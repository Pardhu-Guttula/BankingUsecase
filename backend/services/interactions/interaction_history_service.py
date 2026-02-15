# Epic Title: Interaction History and Documentation Upload

from backend.repositories.interactions.interaction_history_repository import InteractionHistoryRepository
from backend.models.interactions.interaction_history_model import InteractionHistory

class InteractionHistoryService:
    @staticmethod
    def log_interaction(user_id: int, action: str) -> InteractionHistory:
        interaction = InteractionHistory(user_id=user_id, action=action)
        InteractionHistoryRepository.save(interaction)
        return interaction

    @staticmethod
    def get_user_history(user_id: int) -> list[InteractionHistory]:
        return InteractionHistoryRepository.get_history_by_user(user_id)


# File 5: Create Controller to Handle User Interaction History in history/controllers/interaction_history_controller.py