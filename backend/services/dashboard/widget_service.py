# Epic Title: Personalized Dashboard

from backend.models.dashboard.widget_model import Widget
from backend.repositories.dashboard.widget_repository import WidgetRepository

class WidgetService:
    @staticmethod
    def add_widget(user_id: int, widget_type: str) -> Widget:
        widget = Widget(user_id=user_id, widget_type=widget_type)
        WidgetRepository.save(widget)
        return widget

    @staticmethod
    def remove_widget(user_id: int, widget_id: int) -> None:
        widget = Widget.query.filter_by(user_id=user_id, id=widget_id).first()
        if widget:
            WidgetRepository.delete(widget)

    @staticmethod
    def get_user_widgets(user_id: int) -> list[Widget]:
        return WidgetRepository.get_by_user_id(user_id)

# File 4: Widget Controller in controllers/dashboard/widget_controller.py