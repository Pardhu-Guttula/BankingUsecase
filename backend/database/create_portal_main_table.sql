# Epic Title: Core Banking System Integration

CREATE TABLE IF NOT EXISTS portal_main (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data VARCHAR(255) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

# File 7: Update requirements.txt with Required Dependencies