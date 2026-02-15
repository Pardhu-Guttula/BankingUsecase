# Epic Title: Customizable Widgets

from backend.repositories.dashboard.widget_repository import WidgetRepository
from backend.models.dashboard.widget_model import Widget

class WidgetService:
    @staticmethod
    def add_widget(user_id: int, widget_type: str, position: int) -> None:
        widget = Widget(user_id=user_id, widget_type=widget_type, position=position)
        WidgetRepository.save(widget)

    @staticmethod
    def remove_widget(widget_id: int) -> None:
        widget = Widget.query.get(widget_id)
        if widget:
            WidgetRepository.remove(widget)

    @staticmethod
    def get_widgets(user_id: int) -> list:
        return WidgetRepository.find_by_user_id(user_id)


# File 4: Dashboard Controller Updated for Widgets in controllers/dashboard/dashboard_controller.py