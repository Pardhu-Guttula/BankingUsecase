# Epic Title: Document Upload Capability

from backend.repositories.documents.document_repository import DocumentRepository
from backend.models.documents.document_model import Document
from werkzeug.utils import secure_filename
import os

class DocumentService:
    
    UPLOAD_FOLDER = 'backend/uploads/documents'
    ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}

    @staticmethod
    def allowed_file(filename: str) -> bool:
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in DocumentService.ALLOWED_EXTENSIONS

    @staticmethod
    def upload_document(user_id: int, file) -> Document:
        if file and DocumentService.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(DocumentService.UPLOAD_FOLDER, filename)
            file.save(filepath)

            document = Document(user_id=user_id, filename=filename, filepath=filepath)
            DocumentRepository.save(document)
            return document
        else:
            raise ValueError("File type not allowed")


# File 4: Document Upload Controller in `controllers/documents/document_upload_controller.py`