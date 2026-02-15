# Epic Title: Interaction History and Documentation Upload

from backend.models.interactions.document_model import Document

class DocumentRepository:
    @staticmethod
    def save(document: Document) -> None:
        db.session.add(document)
        db.session.commit()

    @staticmethod
    def find_by_user_id(user_id: int) -> list[Document]:
        return Document.query.filter_by(user_id=user_id).all()


# File 5: Document Service to Handle Business Logic in services/interactions/document_service.py