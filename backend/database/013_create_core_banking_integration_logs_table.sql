-- Epic Title: Core Banking System Integration

CREATE TABLE core_banking_integration_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    request_details TEXT NOT NULL,
    response_details TEXT,
    status_code INT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);