# Epic Title: Personalized Dashboard

from backend.models.dashboard.widget_model import Widget

class WidgetRepository:
    @staticmethod
    def find_by_user_id(user_id: int) -> list[Widget]:
        return Widget.query.filter_by(user_id=user_id).all()

    @staticmethod
    def save(widget: Widget) -> None:
        db.session.add(widget)
        db.session.commit()

    @staticmethod
    def delete(widget: Widget) -> None:
        db.session.delete(widget)
        db.session.commit()


# File 4: Widget Service to Handle Business Logic in services/dashboard/widget_service.py