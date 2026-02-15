# Epic Title: Maintain Interaction History

from datetime import datetime
from backend.app import db

class Interaction(db.Model):
    __tablename__ = 'interactions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    action = db.Column(db.String(256), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, user_id: int, action: str):
        self.user_id = user_id
        self.action = action


# File 2: Interaction Repository for Database Operations in interaction_history/repositories/interaction_repository.py