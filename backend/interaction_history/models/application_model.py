# Epic Title: Save and Resume Incomplete Applications

from datetime import datetime
from backend.app import db

class Application(db.Model):
    __tablename__ = 'applications'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    data = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), nullable=False, default='incomplete')
    save_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, user_id: int, data: str, status: str = 'incomplete'):
        self.user_id = user_id
        self.data = data
        self.status = status


# File 2: Application Repository for Database Operations in interaction_history/repositories/application_repository.py