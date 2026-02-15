# Epic Title: Core Banking System Integration

from backend.models.portal_main_database.portal_main_model import PortalMainModel
from backend.repositories.portal_main_database.portal_main_repository import PortalMainRepository

class PortalMainService:
    @staticmethod
    def add_data(data: str) -> PortalMainModel:
        data_entry = PortalMainModel(data=data)
        PortalMainRepository.save(data_entry)
        return data_entry

    @staticmethod
    def get_all_data() -> list[PortalMainModel]:
        return PortalMainRepository.get_all()

# File 4: Portal Database Controller in controllers/portal_main_database/portal_main_controller.py