# Epic Title: Interaction History and Documentation Upload

from werkzeug.utils import secure_filename
from backend.models.documents.document_model import Document
from backend.documents.repositories.document_repository import DocumentRepository
from flask import current_app
import os

class DocumentService:
    @staticmethod
    def save_document(file, user_id: int) -> bool:
        try:
            filename = secure_filename(file.filename)
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            document = Document(user_id=user_id, filename=filename, filepath=filepath)
            DocumentRepository.save(document)
            return True
        except Exception as e:
            current_app.logger.error(f"Document upload failed: {e}")
            return False


# File 4: Document Controller to Expose Document Upload Endpoints in documents/controllers/document_controller.py