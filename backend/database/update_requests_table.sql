# Epic Title: Core Banking System Integration

ALTER TABLE requests
ADD COLUMN external_id VARCHAR(100) NOT NULL UNIQUE;

# File 10: Update Schema for Existing Transactions and Requests Table in database/migrate_existing_transactions_and_requests.sql