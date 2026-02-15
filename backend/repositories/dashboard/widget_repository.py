# Epic Title: Personalized Dashboard

from backend.models.dashboard.widget_model import Widget
from backend.app import db

class WidgetRepository:
    @staticmethod
    def save(widget: Widget) -> None:
        db.session.add(widget)
        db.session.commit()

    @staticmethod
    def delete(widget: Widget) -> None:
        db.session.delete(widget)
        db.session.commit()

    @staticmethod
    def get_by_user_id(user_id: int) -> list[Widget]:
        return Widget.query.filter_by(user_id=user_id).all()

# File 3: Widget Service for Widget Business Logic in services/dashboard/widget_service.py