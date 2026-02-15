# Epic Title: Personalized Dashboard

from backend.repositories.dashboard.widget_repository import WidgetRepository
from backend.models.dashboard.widget_model import Widget

class WidgetService:
    @staticmethod
    def get_user_widgets(user_id: int) -> list[Widget]:
        return WidgetRepository.find_by_user_id(user_id)

    @staticmethod
    def add_widget(user_id: int, widget_name: str, widget_settings: str = None) -> Widget:
        widget = Widget(user_id, widget_name, widget_settings)
        WidgetRepository.save(widget)
        return widget

    @staticmethod
    def remove_widget(widget_id: int, user_id: int) -> bool:
        widget = Widget.query.filter_by(id=widget_id, user_id=user_id).first()
        if widget:
            WidgetRepository.delete(widget)
            return True
        return False


# File 5: Dashboard Controller Update to Handle Widget Requests in controllers/dashboard/dashboard_controller.py