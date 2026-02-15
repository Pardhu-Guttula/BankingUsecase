# Epic Title: Real-time Status Updates and Notifications

CREATE TABLE IF NOT EXISTS email_notifications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    request_id INT NOT NULL,
    user_id INT NOT NULL,
    email VARCHAR(100) NOT NULL,
    subject VARCHAR(255) NOT NULL,
    content VARCHAR(255) NOT NULL,
    sent BOOLEAN DEFAULT FALSE NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);


# File 8: Update requirements.txt with Only Necessary Dependencies