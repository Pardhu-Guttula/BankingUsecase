# Epic Title: Interaction History and Documentation Upload

from backend.history.models.interaction_history import InteractionHistory, db

class InteractionService:
    def __init__(self):
        pass

    def log_interaction(self, user_id: int, action: str) -> InteractionHistory:
        interaction = InteractionHistory(user_id=user_id, action=action)
        db.session.add(interaction)
        db.session.commit()
        return interaction

    def get_interaction_history(self, user_id: int) -> list[InteractionHistory]:
        return InteractionHistory.query.filter_by(user_id=user_id).order_by(InteractionHistory.timestamp.desc()).all()