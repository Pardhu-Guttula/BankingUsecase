-- Epic Title: Core Banking System Integration

CREATE TABLE core_banking_data_sync (
    id INT AUTO_INCREMENT PRIMARY KEY,
    entity VARCHAR(50) NOT NULL,
    last_synced_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);