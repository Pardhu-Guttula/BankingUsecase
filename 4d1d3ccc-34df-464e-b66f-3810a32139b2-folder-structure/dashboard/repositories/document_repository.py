# Epic Title: Interaction History and Documentation Upload

from dashboard.models.document_model import Document
from backend.app import db

class DocumentRepository:
    @staticmethod
    def save(document: Document) -> None:
        db.session.add(document)
        db.session.commit()

    @staticmethod
    def get_documents_by_request_id(request_id: int) -> list[Document]:
        return Document.query.filter_by(request_id=request_id).all()


# File 3: Document Service for Business Logic in dashboard/services/document_service.py