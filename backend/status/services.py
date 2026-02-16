# Epic Title: Real-time Status Updates and Notifications

import logging
from flask_socketio import SocketIO
from backend.status.models import RequestStatus
from backend.access.services.email_service import EmailService
from flask_sqlalchemy import SQLAlchemy

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
        return new_status

    def get_status(self, request_id: int) -> RequestStatus:
        return RequestStatus.query.filter_by(request_id=request_id).order_by(RequestStatus.updated_at.desc()).first()