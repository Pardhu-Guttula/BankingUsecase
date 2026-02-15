# Epic Title: Customizable Widgets

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from ..models.widget import Widget

DATABASE_URI = 'mysql+pymysql://username:password@localhost/db_name'
engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class WidgetService:
    def __init__(self):
        self.db = SessionLocal()

    def add_widget(self, user_id: int, widget_type: str, settings: str) -> bool:
        new_widget = Widget(user_id=user_id, widget_type=widget_type, settings=settings)
        self.db.add(new_widget)
        self.db.commit()
        return True

    def remove_widget(self, user_id: int, widget_id: int) -> bool:
        widget = self.db.query(Widget).filter(Widget.id == widget_id, Widget.user_id == user_id).first()
        if widget:
            self.db.delete(widget)
            self.db.commit()
            return True
        return False

    def get_widgets(self, user_id: int):
        widgets = self.db.query(Widget).filter(Widget.user_id == user_id).all()
        return [{'id': widget.id, 'widget_type': widget.widget_type, 'settings': widget.settings} for widget in widgets]



# File 5: Database Schema for Widgets in database/widgets.sql