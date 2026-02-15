# Epic Title: Service Modification Requests

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from ..models.service_modification_request import ServiceModificationRequest

DATABASE_URI = 'mysql+pymysql://username:password@localhost/db_name'
engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class ServiceModificationRequestService:
    def __init__(self):
        self.db = SessionLocal()

    def create_service_modification_request(self, user_id: int, service_name: str) -> bool:
        new_request = ServiceModificationRequest(user_id=user_id, service_name=service_name)
        self.db.add(new_request)
        self.db.commit()
        return True

    def get_service_modification_requests(self, user_id: int):
        requests = self.db.query(ServiceModificationRequest).filter(ServiceModificationRequest.user_id == user_id).all()
        return [{'id': request.id, 'service_name': request.service_name, 'status': request.status} for request in requests]



# File 5: Database Schema for ServiceModificationRequest in database/service_modification_requests.sql