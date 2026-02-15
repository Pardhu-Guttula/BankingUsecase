# Epic Title: Customizable Widgets

from backend.models.dashboard.widget_model import Widget
from backend.app import db

class WidgetRepository:
    @staticmethod
    def save(widget: Widget) -> None:
        db.session.add(widget)
        db.session.commit()

    @staticmethod
    def remove(widget: Widget) -> None:
        db.session.delete(widget)
        db.session.commit()

    @staticmethod
    def find_by_user_id(user_id: int) -> list[Widget]:
        return Widget.query.filter_by(user_id=user_id).all()


# File 3: Widgets Service in backend/services/dashboard/widget_service.py