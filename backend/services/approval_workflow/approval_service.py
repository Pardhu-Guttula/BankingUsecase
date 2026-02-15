# Epic Title: Account Opening and Service Modifications

from backend.repositories.approval_workflow.approval_repository import ApprovalRepository
from backend.models.approval_workflow.request_approval_model import RequestApproval

class ApprovalService:
    @staticmethod
    def submit_for_approval(request_id: int, request_type: str):
        request_approval = RequestApproval(request_id=request_id, request_type=request_type)
        ApprovalRepository.save(request_approval)

    @staticmethod
    def approve(request_approval_id: int, approver_id: int):
        request_approval = RequestApproval.query.get(request_approval_id)
        if request_approval:
            request_approval.status = 'Approved'
            request_approval.approver_id = approver_id
            ApprovalRepository.update(request_approval)


# File 5: Controller to Handle Approval Workflow in approval_workflow/controllers/approval_controller.py