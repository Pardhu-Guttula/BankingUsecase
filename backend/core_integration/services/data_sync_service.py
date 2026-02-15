# Epic Title: Data Synchronization Mechanisms

import requests
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from core_integration.models.sync_log_model import SyncLog
from typing import Any, Dict
from requests.auth import HTTPBasicAuth
from backend.app import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class DataSyncService:
    BASE_URL = "https://api.corebanking.com"
    API_USERNAME = "api_user"
    API_PASSWORD = "api_password"

    @staticmethod
    def make_request(endpoint: str, method: str = "GET", data: Dict[str, Any] = None) -> Dict[str, Any]:
        url = f"{DataSyncService.BASE_URL}/{endpoint}"
        auth = HTTPBasicAuth(DataSyncService.API_USERNAME, DataSyncService.API_PASSWORD)
        
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        try:
            if method == "GET":
                response = requests.get(url, headers=headers, auth=auth)
            else:
                response = requests.post(url, headers=headers, json=data, auth=auth)
            
            response.raise_for_status()

            DataSyncService.log_sync(endpoint, response.json())

            return response.json()
        except requests.RequestException as e:
            print(f"Request to {url} failed: {e}")
            raise

    @staticmethod
    def log_sync(endpoint: str, response: Dict[str, Any]) -> None:
        session = SessionLocal()
        sync_log = SyncLog(endpoint=endpoint, response_data=response)

        try:
            session.add(sync_log)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Failed to log sync: {e}")
        finally:
            session.close()


# File 2: SyncLog Model for Logging Synchronization Data in core_integration/models/sync_log_model.py