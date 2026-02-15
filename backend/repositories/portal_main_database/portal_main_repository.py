# Epic Title: Maintain Separate Database

from backend.models.portal_main_database.portal_main_model import PortalMainData
from backend.app import db

class PortalMainRepository:
    @staticmethod
    def save(data: PortalMainData) -> None:
        db.session.add(data)
        db.session.commit()

    @staticmethod
    def find_by_key(data_key: str) -> PortalMainData:
        return PortalMainData.query.filter_by(data_key=data_key).first()

    @staticmethod
    def find_all() -> list[PortalMainData]:
        return PortalMainData.query.all()


# File 3: Portal Main Database Service in `services/portal_main_database/portal_main_service.py`