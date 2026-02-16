# Epic Title: Real-time Status Updates and Notifications

import logging
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from backend.status.models import RequestStatus, Notification
from backend.access.services.email_service import EmailService

logger = logging.getLogger(__name__)

class StatusService:
    def __init__(self, db: SQLAlchemy, socketio: SocketIO, email_service: EmailService):
        self.db = db
        self.socketio = socketio
        self.email_service = email_service

    def update_status(self, user_id: int, request_id: int, status: str) -> RequestStatus:
        new_status = RequestStatus(user_id=user_id, request_id=request_id, status=status)
        self.db.session.add(new_status)
        self.db.session.commit()
        logger.info(f"Updated status for request_id: {request_id} to {status}")

        # Emit real-time update to the user
        self.socketio.emit('status_update', {'request_id': request_id, 'status': status}, room=user_id)

        # Send email notification
        self.email_service.send_status_update_email(user_id, request_id, status)

        # Create in-app notification
        message = f"Status of your request {request_id} has been updated to '{status}'."
        self.create_notification(user_id, message)

        return new_status

    def create_notification(self, user_id: int, message: str) -> Notification:
        notification = Notification(user_id=user_id, message=message)
        self.db.session.add(notification)
        self.db.session.commit()
        logger.info(f"Created in-app notification for user_id: {user_id}")
        self.socketio.emit('new_notification', {'message': message}, room=user_id)
        return notification

    def get_status(self, request_id: int) -> RequestStatus:
        return RequestStatus.query.filter_by(request_id=request_id).order_by(RequestStatus.updated_at.desc()).first()

    def get_notifications(self, user_id: int) -> list[Notification]:
        return Notification.query.filter_by(user_id=user_id, is_read=False).order_by(Notification.created_at.desc()).all()

    def mark_notification_as_read(self, notification_id: int) -> None:
        notification = Notification.query.get(notification_id)
        if notification:
            notification.is_read = True
            self.db.session.commit()
            logger.info(f"Marked notification {notification_id} as read")
        else:
            logger.warning(f"Notification {notification_id} not found")