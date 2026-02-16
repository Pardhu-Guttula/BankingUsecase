# Epic Title: Interaction History and Documentation Upload

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Document(db.Model):
    __tablename__ = "documents"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    request_id: int = db.Column(db.Integer, nullable=False)
    filename: str = db.Column(db.String(255), nullable=False)
    filepath: str = db.Column(db.String(255), nullable=False)
    uploaded_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Document {self.id} for request {self.request_id}>"