# Epic Title: Interaction History and Documentation Upload

import os
import logging
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from backend.documents.models import Document

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
logger = logging.getLogger(__name__)

class DocumentService:
    def __init__(self, db: SQLAlchemy, upload_folder: str = UPLOAD_FOLDER):
        self.db = db
        self.upload_folder = upload_folder

    def allowed_file(self, filename: str) -> bool:
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def save_document(self, user_id: int, request_id: int, file) -> Document:
        if file and self.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(self.upload_folder, filename)
            file.save(filepath)

            document = Document(user_id=user_id, request_id=request_id, filename=filename, filepath=filepath)
            self.db.session.add(document)
            self.db.session.commit()
            logger.info(f"Document saved: {document.filename}")

            return document
        else:
            logger.error(f"Invalid file format: {file.filename}")
            raise ValueError("Invalid file format")

    def get_documents(self, request_id: int) -> list[Document]:
        return Document.query.filter_by(request_id=request_id).order_by(Document.uploaded_at.desc()).all()

    def get_document_path(self, document_id: int) -> str:
        document = Document.query.get(document_id)
        return document.filepath if document else None