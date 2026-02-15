# Epic Title: Interaction History and Documentation Upload

from backend.models.documents.document_model import Document
from backend.app import db

class DocumentRepository:
    @staticmethod
    def save(document: Document) -> None:
        db.session.add(document)
        db.session.commit()


# File 3: Document Service to Handle Business Logic of Document Uploading in documents/services/document_service.py