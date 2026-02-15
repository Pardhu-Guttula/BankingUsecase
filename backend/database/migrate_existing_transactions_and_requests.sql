# Epic Title: Core Banking System Integration

UPDATE transactions
SET external_id = CONCAT('txn-', id)
WHERE external_id IS NULL;

UPDATE requests
SET external_id = CONCAT('req-', id)
WHERE external_id IS NULL;

# File 11: Update requirements.txt with Required Dependencies