# Epic Title: Core Banking System Integration

from backend.models.portal_main_database.portal_main_model import PortalMainModel
from backend.app import db

class PortalMainRepository:
    @staticmethod
    def save(data_entry: PortalMainModel) -> None:
        db.session.add(data_entry)
        db.session.commit()

    @staticmethod
    def get_all() -> list[PortalMainModel]:
        return PortalMainModel.query.all()

# File 3: Portal Database Service in services/portal_main_database/portal_main_service.py