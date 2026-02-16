# Epic Title: Customizable Widgets

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Widget(db.Model):
    __tablename__ = "widgets"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    widget_type: str = db.Column(db.String(50), nullable=False)
    settings: str = db.Column(db.String(255), nullable=True)
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Widget {self.widget_type} for user {self.user_id}>"