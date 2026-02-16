# Epic Title: Interaction History and Documentation Upload

import os
from werkzeug.utils import secure_filename
from backend.documents.models.document import Document, db

class DocumentService:
    def __init__(self, upload_folder: str):
        self.upload_folder = upload_folder

    def save_document(self, request_id: int, file) -> Document:
        filename = secure_filename(file.filename)
        filepath = os.path.join(self.upload_folder, filename)
        file.save(filepath)

        document = Document(request_id=request_id, filename=filename, filepath=filepath)
        db.session.add(document)
        db.session.commit()
        return document

    def get_documents_for_request(self, request_id: int) -> list[Document]:
        return Document.query.filter_by(request_id=request_id).all()