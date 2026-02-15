# Epic Title: Personalized Dashboard

from backend.models.dashboard.widget_model import Widget
from backend.account.repositories.widget_repository import WidgetRepository
from backend.app import db

class WidgetService:
    @staticmethod
    def add_widget(user_id: int, name: str, settings: str) -> bool:
        try:
            widget = Widget(user_id=user_id, name=name, settings=settings)
            WidgetRepository.save(widget)
            return True
        except Exception as e:
            db.session.rollback()
            return False

    @staticmethod
    def remove_widget(widget_id: int) -> bool:
        try:
            widget = Widget.query.get(widget_id)
            if widget:
                WidgetRepository.delete(widget)
                return True
            return False
        except Exception as e:
            db.session.rollback()
            return False


# File 4: Widget Controller to Manage Widget API Endpoints in account/controllers/widget_controller.py