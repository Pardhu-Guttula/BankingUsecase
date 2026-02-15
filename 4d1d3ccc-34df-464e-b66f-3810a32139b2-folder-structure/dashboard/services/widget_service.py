# Epic Title: Customizable Widgets

from dashboard.repositories.widget_repository import WidgetRepository
from dashboard.models.widget_model import Widget

class WidgetService:
    @staticmethod
    def get_user_widgets(user_id: int) -> list:
        widgets = WidgetRepository.get_widgets_by_user_id(user_id)
        return [{
            "id": widget.id,
            "name": widget.name,
            "settings": widget.settings
        } for widget in widgets]

    @staticmethod
    def add_widget(user_id: int, name: str, settings: str) -> Widget:
        widget = Widget(user_id, name, settings)
        WidgetRepository.save(widget)
        return widget

    @staticmethod
    def remove_widget(widget_id: int) -> bool:
        widget = WidgetRepository.get_widget_by_id(widget_id)
        if widget:
            WidgetRepository.delete(widget)
            return True
        return False


# File 4: Widget Controller for Handling Requests in dashboard/controllers/widget_controller.py