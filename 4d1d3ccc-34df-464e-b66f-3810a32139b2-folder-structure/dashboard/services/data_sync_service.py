# Epic Title: Core Banking System Integration

import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
from typing import Any, Dict
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from backend.app import db

class DataSyncService:
    _last_sync_time: datetime = None

    @staticmethod
    def fetch_core_banking_data(endpoint: str) -> Any:
        core_banking_api_url = "https://api.corebanking.com"
        username = "your_api_username"
        password = "your_api_password"
        full_url = f"{core_banking_api_url}/{endpoint}"
        
        response = requests.get(
            full_url,
            auth=HTTPBasicAuth(username, password),
            timeout=30
        )
        response.raise_for_status()
        return response.json()

    @staticmethod
    def sync_data() -> None:
        data = DataSyncService.fetch_core_banking_data("sync")
        
        # Assuming data contains list of items to update in the portal DB
        session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=create_engine(db)))
        
        try:
            # Example of updating customers data
            for item in data['customers']:
                # Assuming we have a Customer model with the required fields
                customer = Customer.query.filter_by(id=item['id']).first()
                if customer:
                    customer.update_from_dict(item)
                else:
                    customer = Customer(**item)
                    session.add(customer)
            
            session.commit()
            DataSyncService._last_sync_time = datetime.utcnow()
        except Exception as e:
            session.rollback()
            print(f"Error during data sync: {e}")
            raise
        finally:
            session.remove()

    @staticmethod
    def get_last_sync_time() -> datetime:
        return DataSyncService._last_sync_time


# File 2: Data Sync Controller for Triggering Sync in dashboard/controllers/data_sync_controller.py