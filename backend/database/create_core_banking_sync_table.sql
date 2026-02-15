# Epic Title: Data Synchronization Mechanisms

CREATE TABLE IF NOT EXISTS core_banking_sync (
    id INT AUTO_INCREMENT PRIMARY KEY,
    entity VARCHAR(255) NOT NULL,
    last_synced DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);


# File 6: Update `app.py` to Register Core Banking Sync Controller