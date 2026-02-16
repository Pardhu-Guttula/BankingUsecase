# Epic Title: Interaction History and Documentation Upload

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class IncompleteApplication(db.Model):
    __tablename__ = "incomplete_applications"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    data: str = db.Column(db.Text, nullable=False)  # JSON string
    saved_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<IncompleteApplication {self.id} - {self.user_id} - {self.saved_at}>"