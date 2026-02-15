# Epic Title: Real-time Status Updates and Notifications

from backend.models.notifications.status_update_model import StatusUpdate

class StatusUpdateRepository:
    @staticmethod
    def save(update: StatusUpdate) -> None:
        db.session.add(update)
        db.session.commit()

    @staticmethod
    def find_by_user_id(user_id: int) -> list[StatusUpdate]:
        return StatusUpdate.query.filter_by(user_id=user_id).all()


# File 4: StatusUpdateService to Handle Status Update Logic in services/notifications/status_update_service.py