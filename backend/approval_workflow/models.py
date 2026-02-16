# Epic Title: Approval and Processing Workflows

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ApprovalWorkflow(db.Model):
    __tablename__ = "approval_workflows"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    request_id: int = db.Column(db.Integer, nullable=False)
    request_type: str = db.Column(db.String(50), nullable=False)  # 'account_opening', 'service_modification'
    status: str = db.Column(db.String(20), default='pending')  # 'pending', 'approved', 'rejected'
    processed_at: datetime = db.Column(db.DateTime, nullable=True)
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<ApprovalWorkflow {self.id} - {self.request_type} - {self.status}>"