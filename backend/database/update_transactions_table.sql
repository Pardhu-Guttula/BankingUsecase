# Epic Title: Core Banking System Integration

ALTER TABLE transactions
ADD COLUMN external_id VARCHAR(100) NOT NULL UNIQUE;

# File 9: Update Schema for Requests Table to Add External ID in database/update_requests_table.sql