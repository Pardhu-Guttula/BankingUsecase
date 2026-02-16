# Epic Title: Real-time Status Updates

import logging
from datetime import datetime
from flask_socketio import SocketIO
from typing import Optional
from backend.status.models import RequestStatus

logger = logging.getLogger(__name__)

class StatusService:
    def __init__(self, db, socketio: SocketIO):
        self.db = db
        self.socketio = socketio

    def update_status(self, user_id: int, request_id: int, status: str) -> RequestStatus:
        new_status = RequestStatus(user_id=user_id, request_id=request_id, status=status)
        self.db.session.add(new_status)
        self.db.session.commit()
        logger.info(f"Updated status for request_id: {request_id} to {status}")

        # Emit real-time update to the user
        self.socketio.emit('status_update', {'request_id': request_id, 'status': status}, room=user_id)
        return new_status

    def get_status(self, request_id: int) -> Optional[RequestStatus]:
        return RequestStatus.query.filter_by(request_id=request_id).order_by(RequestStatus.updated_at.desc()).first()