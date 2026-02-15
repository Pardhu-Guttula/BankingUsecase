# Epic Title: Real-time Status Updates and Notifications

CREATE TABLE IF NOT EXISTS notifications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    request_id INT NOT NULL,
    message VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (request_id) REFERENCES requests(id)
);

# File 7: Update requirements.txt with Only Necessary Dependencies