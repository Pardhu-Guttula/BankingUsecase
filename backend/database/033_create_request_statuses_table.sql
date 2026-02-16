-- Epic Title: Real-time Status Updates

CREATE TABLE request_statuses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    request_id INT NOT NULL,
    status VARCHAR(20) NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);