# Epic Title: Personalized Dashboard

from backend.models.dashboard.widget_model import Widget
from backend.repositories.dashboard.widget_repository import WidgetRepository

class WidgetService:
    @staticmethod
    def add_widget(user_id: int, name: str, position: int) -> Widget:
        widget = Widget(user_id=user_id, name=name, position=position)
        WidgetRepository.save(widget)
        return widget

    @staticmethod
    def remove_widget(widget_id: int) -> None:
        widget = WidgetRepository.get_by_id(widget_id)
        if widget:
            WidgetRepository.delete(widget)

    @staticmethod
    def get_user_widgets(user_id: int) -> list[Widget]:
        return WidgetRepository.get_by_user_id(user_id)

# File 4: Widget Controller to Handle Requests in controllers/dashboard/widget_controller.py