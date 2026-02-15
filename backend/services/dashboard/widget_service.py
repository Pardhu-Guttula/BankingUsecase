# Epic Title: Personalized Dashboard

from backend.models.dashboard.widget_model import Widget
from backend.repositories.dashboard.widget_repository import WidgetRepository


class WidgetService:
    @staticmethod
    def add_widget(user_id: int, widget_type: str, position: int) -> Widget:
        widget = Widget(user_id=user_id, widget_type=widget_type, position=position)
        WidgetRepository.save(widget)
        return widget

    @staticmethod
    def remove_widget(user_id: int, widget_id: int) -> None:
        widget = Widget.query.filter_by(id=widget_id, user_id=user_id).first()
        if widget:
            WidgetRepository.delete(widget)

    @staticmethod
    def get_user_widgets(user_id: int) -> list[Widget]:
        return WidgetRepository.get_widgets_by_user_id(user_id)


# File 4: Widget Controller to Manage Widget Addition and Removal in dashboard/controllers/widget_controller.py