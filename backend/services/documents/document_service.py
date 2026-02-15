# Epic Title: Interaction History and Documentation Upload

import os
from werkzeug.utils import secure_filename
from backend.repositories.documents.document_repository import DocumentRepository
from backend.models.documents.document_model import Document
from flask import current_app

class DocumentService:
    @staticmethod
    def allowed_file(filename: str) -> bool:
        allowed_extensions = {'pdf', 'png', 'jpg', 'jpeg', 'doc', 'docx'}
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

    @staticmethod
    def upload_document(file, user_id: int) -> Document:
        if file and DocumentService.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            document = Document(user_id=user_id, filename=filename, path=file_path)
            DocumentRepository.save(document)
            return document


# File 5: Controller to Handle Document Upload in documents/controllers/document_controller.py