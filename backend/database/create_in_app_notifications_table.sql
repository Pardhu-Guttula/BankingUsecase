# Epic Title: Real-time Status Updates and Notifications

CREATE TABLE IF NOT EXISTS in_app_notifications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    message VARCHAR(255) NOT NULL,
    timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    seen INT NOT NULL DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

# File 8: Update requirements.txt with Required Dependency