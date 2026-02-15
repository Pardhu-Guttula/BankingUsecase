# Epic Title: Maintain Separate Database

from backend.repositories.portal_main_database.portal_main_repository import PortalMainRepository
from backend.models.portal_main_database.portal_main_model import PortalMainData

class PortalMainService:
    @staticmethod
    def save_data(data_key: str, data_value: str) -> None:
        data = PortalMainData(data_key=data_key, data_value=data_value)
        PortalMainRepository.save(data)

    @staticmethod
    def get_data_by_key(data_key: str) -> PortalMainData:
        return PortalMainRepository.find_by_key(data_key)

    @staticmethod
    def get_all_data() -> list[PortalMainData]:
        return PortalMainRepository.find_all()


# File 4: Portal Main Database Controller in `controllers/portal_main_database/portal_main_controller.py`