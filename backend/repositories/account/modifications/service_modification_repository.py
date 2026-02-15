# Epic Title: Account Opening and Service Modifications

from backend.models.account.modifications.service_modification_model import ServiceModification
from backend.app import db

class ServiceModificationRepository:
    @staticmethod
    def save(service_modification: ServiceModification) -> None:
        db.session.add(service_modification)
        db.session.commit()

    @staticmethod
    def get_by_user_id(user_id: int) -> list[ServiceModification]:
        return ServiceModification.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_by_id(service_modification_id: int) -> ServiceModification:
        return ServiceModification.query.filter_by(id=service_modification_id).first()

    @staticmethod
    def update_status(service_modification_id: int, status: str) -> None:
        service_modification = ServiceModificationRepository.get_by_id(service_modification_id)
        if service_modification:
            service_modification.status = status
            db.session.commit()

# File 3: Service Modification Service in services/account/modifications/service_modification_service.py