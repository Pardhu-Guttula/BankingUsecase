# Epic Title: Real-time Status Updates and Notifications

CREATE TABLE status_updates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    request_id INT NOT NULL,
    status VARCHAR(50) NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (request_id) REFERENCES service_modification_requests(id) ON DELETE CASCADE
);


# File 7: requirements.txt Update