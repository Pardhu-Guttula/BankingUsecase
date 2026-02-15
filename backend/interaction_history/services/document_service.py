# Epic Title: Document Upload Capability

from werkzeug.datastructures import FileStorage
from backend.interaction_history.repositories.document_repository import DocumentRepository
from backend.interaction_history.models.document_model import Document
import os

class DocumentService:
    UPLOAD_FOLDER = '/path/to/upload/folder'

    @staticmethod
    def save_document(file: FileStorage, user_id: int) -> str:
        filename = file.filename
        save_path = os.path.join(DocumentService.UPLOAD_FOLDER, filename)
        file.save(save_path)
        document = Document(user_id=user_id, filename=filename)
        DocumentRepository.save_document(document)
        return filename

    @staticmethod
    def get_user_documents(user_id: int) -> list[Document]:
        return DocumentRepository.get_documents_by_user(user_id)


# File 4: Document Upload Endpoint in interaction_history/controllers/document_controller.py