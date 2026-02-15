# Epic Title: Real-time Status Updates and Notifications

CREATE TABLE IF NOT EXISTS statuses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    request_id INT NOT NULL,
    status VARCHAR(50) NOT NULL,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (request_id) REFERENCES requests(id)
);

# File 7: Update requirements.txt with Only Necessary Dependencies