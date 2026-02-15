# Epic Title: Core Banking System Integration

CREATE TABLE IF NOT EXISTS core_banking_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    entity_id INT NOT NULL,
    entity_type VARCHAR(255) NOT NULL,
    data TEXT NOT NULL,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
);


# File 7: Update requirements.txt with Only Necessary Dependencies