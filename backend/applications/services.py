# Epic Title: Interaction History and Documentation Upload

import logging
from flask_sqlalchemy import SQLAlchemy
from backend.applications.models import IncompleteApplication

logger = logging.getLogger(__name__)

class ApplicationService:
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def save_incomplete_application(self, user_id: int, data: str) -> IncompleteApplication:
        application = IncompleteApplication(user_id=user_id, data=data)
        existing_application = IncompleteApplication.query.filter_by(user_id=user_id).first()
        
        if existing_application:
            existing_application.data = data
            db.session.commit()
            logger.info(f"Updated existing incomplete application for user_id: {user_id}")
            return existing_application
        else:
            self.db.session.add(application)
            self.db.session.commit()
            logger.info(f"Saved new incomplete application for user_id: {user_id}")
            return application

    def get_incomplete_application(self, user_id: int) -> IncompleteApplication:
        return IncompleteApplication.query.filter_by(user_id=user_id).first()