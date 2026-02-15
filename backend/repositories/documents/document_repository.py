# Epic Title: Interaction History and Documentation Upload

from backend.models.documents.document_model import Document
from backend.app import db

class DocumentRepository:
    @staticmethod
    def save(document: Document) -> None:
        db.session.add(document)
        db.session.commit()


# File 4: Document Service Layer in services/documents/document_service.py