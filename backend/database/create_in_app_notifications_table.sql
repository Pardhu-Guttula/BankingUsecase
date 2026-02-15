# Epic Title: Real-time Status Updates and Notifications

CREATE TABLE IF NOT EXISTS in_app_notifications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    message TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);


# File 8: Update requirements.txt with Only Necessary Dependencies