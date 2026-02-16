# Epic Title: Core Banking System Integration

import logging
from datetime import datetime, timedelta
from typing import Optional
from flask_sqlalchemy import SQLAlchemy
from backend.integration.models import CoreBankingDataSync, LocalTransaction
from backend.integration.services import CoreBankingService

logger = logging.getLogger(__name__)

class DataSyncService:
    def __init__(self, db: SQLAlchemy, core_banking_service: CoreBankingService):
        self.db = db
        self.core_banking_service = core_banking_service

    def get_last_sync_time(self, entity: str) -> Optional[datetime]:
        sync_record = CoreBankingDataSync.query.filter_by(entity=entity).first()
        if sync_record:
            return sync_record.last_synced_at
        return None

    def update_sync_time(self, entity: str, timestamp: datetime):
        sync_record = CoreBankingDataSync.query.filter_by(entity=entity).first()
        if sync_record:
            sync_record.last_synced_at = timestamp
        else:
            sync_record = CoreBankingDataSync(entity=entity, last_synced_at=timestamp)
            self.db.session.add(sync_record)
        self.db.session.commit()
        logger.info(f"Updated sync time for {entity}: {timestamp}")

    def fetch_and_sync_data(self, entity: str):
        last_sync_time = self.get_last_sync_time(entity) or datetime.utcnow() - timedelta(days=1)
        current_time = datetime.utcnow()

        # Implement the logic to fetch data from core banking system using CoreBankingService
        # For example, fetch transactions updated after last_sync_time
        try:
            data = self.core_banking_service.make_request(endpoint=f'/sync/{entity}', method='GET', data={'since': last_sync_time})
            
            # Process and save the fetched data to the local database
            self._process_and_save_data(entity, data)

            # Update the last sync time
            self.update_sync_time(entity, current_time)
        except Exception as e:
            logger.error(f"Failed to sync data for entity {entity}. Error: {str(e)}")

    def _process_and_save_data(self, entity: str, data: dict):
        # Placeholder function to process and save data
        if entity == 'transactions':
            for txn in data:
                local_txn = LocalTransaction(
                    user_id=txn['user_id'],
                    amount=txn['amount'],
                    transaction_type=txn['transaction_type'],
                    status=txn['status'],
                    timestamp=datetime.strptime(txn['timestamp'], '%Y-%m-%dT%H:%M:%S')
                )
                self.db.session.add(local_txn)
            self.db.session.commit()
            logger.info(f"Data for {entity} processed and saved successfully.")