# Epic Title: Data Synchronization Mechanisms

from backend.app import db
from datetime import datetime

class SyncLog(db.Model):
    __tablename__ = 'sync_logs'

    id = db.Column(db.Integer, primary_key=True)
    endpoint = db.Column(db.String(256), nullable=False)
    response_data = db.Column(db.JSON, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, endpoint: str, response_data: dict):
        self.endpoint = endpoint
        self.response_data = response_data


# File 3: Data Sync Controller to Invoke Synchronization in core_integration/controllers/data_sync_controller.py