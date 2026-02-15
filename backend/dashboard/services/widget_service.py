# Epic Title: Personalized Dashboard

from backend.dashboard.repositories.widget_repository import WidgetRepository
from backend.models.dashboard.widget_model import Widget

class WidgetService:
    @staticmethod
    def add_widget(user_id: int, name: str, config: str) -> Widget:
        widget = Widget(user_id, name, config)
        WidgetRepository.save(widget)
        return widget

    @staticmethod
    def remove_widget(widget_id: int) -> None:
        widget = WidgetRepository.find_by_id(widget_id)
        if widget:
            WidgetRepository.delete(widget)

    @staticmethod
    def get_widgets_by_user(user_id: int) -> list[Widget]:
        return WidgetRepository.find_by_user_id(user_id)


# File 4: Add Widgets to Dashboard Controller for Widget Management in dashboard/controllers/dashboard_controller.py