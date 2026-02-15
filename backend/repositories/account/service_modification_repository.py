# Epic Title: Account Opening and Service Modifications

from backend.models.account.service_modification_model import ServiceModification
from backend.app import db

class ServiceModificationRepository:
    @staticmethod
    def get_service_modifications_by_user(user_id: int) -> list[ServiceModification]:
        return ServiceModification.query.filter_by(user_id=user_id).all()

    @staticmethod
    def save(service_modification: ServiceModification) -> None:
        db.session.add(service_modification)
        db.session.commit()

    @staticmethod
    def update(service_modification: ServiceModification) -> None:
        db.session.commit()


# File 5: Service Layer for Service Modification in services/account/modifications/service_modification_service.py