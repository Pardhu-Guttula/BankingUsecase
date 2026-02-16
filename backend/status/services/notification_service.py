# Epic Title: Real-time Status Updates and Notifications

from backend.status.models.notification import Notification, db

class NotificationService:
    def __init__(self, db_session):
        self.db_session = db_session

    def create_notification(self, user_id: int, message: str) -> Notification:
        notification = Notification(user_id=user_id, message=message)
        self.db_session.add(notification)
        self.db_session.commit()
        return notification

    def get_unread_notifications(self, user_id: int) -> list[Notification]:
        return Notification.query.filter_by(user_id=user_id, is_read=False).all()

    def mark_as_read(self, notification_ids: list[int]) -> None:
        notifications = Notification.query.filter(Notification.id.in_(notification_ids)).all()
        for notification in notifications:
            notification.is_read = True
        self.db_session.commit()