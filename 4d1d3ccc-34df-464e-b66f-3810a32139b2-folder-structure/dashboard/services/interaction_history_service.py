# Epic Title: Interaction History and Documentation Upload

from dashboard.repositories.interaction_history_repository import InteractionHistoryRepository
from dashboard.models.interaction_history_model import InteractionHistory

class InteractionHistoryService:
    @staticmethod
    def log_interaction(user_id: int, action: str) -> InteractionHistory:
        interaction = InteractionHistory(user_id=user_id, action=action)
        InteractionHistoryRepository.save(interaction)
        return interaction

    @staticmethod
    def get_user_interactions(user_id: int) -> list:
        interactions = InteractionHistoryRepository.get_interactions_by_user_id(user_id)
        return [{
            "id": interaction.id,
            "action": interaction.action,
            "timestamp": interaction.timestamp
        } for interaction in interactions]


# File 4: Interaction History Controller for Handling Requests in dashboard/controllers/interaction_history_controller.py