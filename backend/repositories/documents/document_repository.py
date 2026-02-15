# Epic Title: Document Upload Capability

from backend.models.documents.document_model import Document
from backend.app import db

class DocumentRepository:
    
    @staticmethod
    def save(document: Document) -> None:
        db.session.add(document)
        db.session.commit()

    @staticmethod
    def find_by_user_id(user_id: int) -> list[Document]:
        return Document.query.filter_by(user_id=user_id).order_by(Document.uploaded_at.desc()).all()


# File 3: Document Upload Service in `services/documents/document_service.py`