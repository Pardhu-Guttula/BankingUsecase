# Epic Title: Interaction History and Documentation Upload

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class InteractionHistory(db.Model):
    __tablename__ = "interaction_history"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id: int = db.Column(db.Integer, nullable=False)
    action: str = db.Column(db.String(255), nullable=False)
    timestamp: datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<InteractionHistory {self.id} for user {self.user_id}>"