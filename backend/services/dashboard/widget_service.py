# Epic Title: Personalized Dashboard

from backend.repositories.dashboard.widget_repository import WidgetRepository
from backend.models.dashboard.widget_model import Widget

class WidgetService:
    @staticmethod
    def add_widget(user_id: int, widget_type: str, widget_data: str = None) -> Widget:
        widget = Widget(user_id=user_id, widget_type=widget_type, widget_data=widget_data)
        WidgetRepository.save(widget)
        return widget

    @staticmethod
    def remove_widget(widget_id: int) -> None:
        widget = Widget.query.get(widget_id)
        if widget:
            WidgetRepository.delete(widget)

    @staticmethod
    def get_widgets(user_id: int) -> list[Widget]:
        return WidgetRepository.get_widgets_by_user(user_id)


# File 5: Controller to handle Widget Management in controllers/dashboard/widget_controller.py