# Epic Title: Interaction History and Documentation Upload

from dashboard.repositories.document_repository import DocumentRepository
from dashboard.models.document_model import Document
from werkzeug.datastructures import FileStorage

class DocumentService:
    @staticmethod
    def upload_document(user_id: int, request_id: int, file: FileStorage) -> Document:
        filename = file.filename
        file_data = file.read()
        document = Document(user_id, request_id, filename, file_data)
        DocumentRepository.save(document)
        return document

    @staticmethod
    def get_request_documents(request_id: int) -> list:
        documents = DocumentRepository.get_documents_by_request_id(request_id)
        return [{
            "id": document.id,
            "filename": document.filename,
            "uploaded_at": document.uploaded_at
        } for document in documents]


# File 4: Document Upload Controller for Handling Requests in dashboard/controllers/document_upload_controller.py