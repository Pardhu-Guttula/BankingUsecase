# Epic Title: Approval and Processing Workflows

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class ApprovalWorkflow(Base):
    __tablename__ = 'approval_workflows'

    id = Column(Integer, primary_key=True)
    request_id = Column(Integer, nullable=False)
    request_type = Column(String(50), nullable=False)
    status = Column(String(20), default='pending')
    approver = Column(String(50))

    def __repr__(self) -> str:
        return f"<ApprovalWorkflow(request_id='{self.request_id}', request_type='{self.request_type}', status='{self.status}', approver='{self.approver}')>"


# File 2: AccountRequest Service Update in account/services/account_request_service.py