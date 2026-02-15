# Epic Title: Personalized Dashboard

from typing import List
from backend.repositories.dashboard.widget_repository import WidgetRepository
from backend.models.dashboard.widget_model import Widget

class WidgetService:
    @staticmethod
    def get_user_widgets(user_id: int) -> List[Widget]:
        return WidgetRepository.get_widgets_by_user(user_id)

    @staticmethod
    def add_widget_to_user(user_id: int, widget_type: str) -> Widget:
        new_widget = Widget(user_id=user_id, widget_type=widget_type)
        WidgetRepository.save(new_widget)
        return new_widget

    @staticmethod
    def remove_widget_from_user(user_id: int, widget_id: int) -> bool:
        widget = Widget.query.filter_by(user_id=user_id, id=widget_id).first()
        if widget:
            WidgetRepository.delete(widget)
            return True
        return False


# File 4: Widget Controller to Handle Widget Endpoints in controllers/dashboard/widget_controller.py