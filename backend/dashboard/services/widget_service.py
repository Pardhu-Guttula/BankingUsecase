# Epic Title: Customizable Widgets

import logging
from typing import List
from backend.dashboard.models.widget import Widget
from backend.authentication.models.user import User

logger = logging.getLogger(__name__)

class WidgetService:
    def __init__(self, db):
        self.db = db
    
    def get_widgets_by_user_id(self, user_id: int) -> List[Widget]:
        widgets = Widget.query.filter_by(user_id=user_id).all()
        logger.info(f"Retrieved {len(widgets)} widgets for user_id: {user_id}")
        return widgets
    
    def add_widget(self, user_id: int, widget_type: str, settings: str) -> Widget:
        widget = Widget(user_id=user_id, widget_type=widget_type, settings=settings)
        self.db.session.add(widget)
        self.db.session.commit()
        logger.info(f"Added widget {widget_type} for user_id: {user_id}")
        return widget
    
    def remove_widget(self, widget_id: int) -> bool:
        widget = Widget.query.get(widget_id)
        if widget:
            self.db.session.delete(widget)
            self.db.session.commit()
            logger.info(f"Removed widget {widget.id} for user_id: {widget.user_id}")
            return True
        logger.warning(f"Widget with id {widget_id} not found")
        return False