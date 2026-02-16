# Epic Title: Interaction History and Documentation Upload

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class IncompleteApplication(db.Model):
    __tablename__ = "incomplete_applications"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id: int = db.Column(db.Integer, nullable=False)
    form_data: str = db.Column(db.Text, nullable=False)
    saved_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<IncompleteApplication {self.id} for user {self.user_id}>"