# Epic Title: Real-time Status Updates

CREATE TABLE IF NOT EXISTS request_statuses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    request_id INT NOT NULL,
    status VARCHAR(50) NOT NULL,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    request_type VARCHAR(50) NOT NULL
);


# File 6: Update app.py to Register Status Update Blueprint