# Epic Title: Maintain Interaction History

import logging
from flask_sqlalchemy import SQLAlchemy
from backend.history.models import InteractionHistory

logger = logging.getLogger(__name__)

class InteractionHistoryService:
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def log_interaction(self, user_id: int, action: str) -> InteractionHistory:
        new_history = InteractionHistory(user_id=user_id, action=action)
        self.db.session.add(new_history)
        self.db.session.commit()
        logger.info(f"Logged interaction for user_id: {user_id} - action: {action}")
        return new_history

    def get_interaction_history(self, user_id: int) -> list[InteractionHistory]:
        return InteractionHistory.query.filter_by(user_id=user_id).order_by(InteractionHistory.timestamp.desc()).all()