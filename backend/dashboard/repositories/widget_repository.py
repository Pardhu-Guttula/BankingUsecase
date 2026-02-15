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
    def find_by_user_id(user_id: int) -> list[Widget]:
        return Widget.query.filter_by(user_id=user_id).all()

    @staticmethod
    def find_by_id(widget_id: int) -> Widget:
        return Widget.query.get(widget_id)


# File 3: Widget Service to Handle Widget Logic in dashboard/services/widget_service.py