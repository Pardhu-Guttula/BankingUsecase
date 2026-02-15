# Epic Title: Interaction History and Documentation Upload

from backend.models.documents.document_model import Document
from backend.repositories.documents.document_repository import DocumentRepository
import os

class DocumentService:
    @staticmethod
    def save_document(file, user_id: int) -> Document:
        filename = file.filename
        file_path = os.path.join('uploads', filename)
        file.save(file_path)
        
        document = Document(
            user_id=user_id,
            filename=filename,
            file_path=file_path
        )
        DocumentRepository.save(document)
        return document

    @staticmethod
    def get_user_documents(user_id: int) -> list[Document]:
        return DocumentRepository.get_by_user_id(user_id)

# File 4: Document Upload Controller in controllers/documents/document_upload_controller.py