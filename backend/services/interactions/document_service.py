# Epic Title: Interaction History and Documentation Upload

import os
from werkzeug.utils import secure_filename
from backend.repositories.interactions.document_repository import DocumentRepository
from backend.models.interactions.document_model import Document

class DocumentService:
    UPLOAD_FOLDER = 'uploads/'

    @staticmethod
    def upload_document(user_id: int, request_id: int, file) -> Document:
        filename = secure_filename(file.filename)
        file_path = os.path.join(DocumentService.UPLOAD_FOLDER, filename)
        file.save(file_path)

        document = Document(user_id, request_id, file.filename, file_path)
        DocumentRepository.save(document)
        return document

    @staticmethod
    def get_user_documents(user_id: int) -> list[Document]:
        return DocumentRepository.find_by_user_id(user_id)


# File 6: Document Controller to Handle Upload Requests in controllers/dashboard/document_controller.py