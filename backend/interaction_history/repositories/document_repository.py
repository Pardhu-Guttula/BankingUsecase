# Epic Title: Document Upload Capability

from backend.interaction_history.models.document_model import Document
from backend.app import db

class DocumentRepository:
    @staticmethod
    def save_document(document: Document) -> None:
        db.session.add(document)
        db.session.commit()

    @staticmethod
    def get_documents_by_user(user_id: int) -> list[Document]:
        return Document.query.filter_by(user_id=user_id).all()


# File 3: Document Service for Business Logic in interaction_history/services/document_service.py