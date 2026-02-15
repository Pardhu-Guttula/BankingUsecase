# Epic Title: Core Banking System Integration

CREATE TABLE IF NOT EXISTS data_sync_statuses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    entity VARCHAR(255) NOT NULL,
    last_synced_at DATETIME NOT NULL,
    status VARCHAR(255) NOT NULL,
    is_success BOOLEAN DEFAULT TRUE
);


# File 7: Update requirements.txt with Only Necessary Dependencies