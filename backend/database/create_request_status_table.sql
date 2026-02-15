# Epic Title: Real-time Status Updates and Notifications

CREATE TABLE IF NOT EXISTS request_statuses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    request_id INT NOT NULL,
    status VARCHAR(20) NOT NULL,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);


# File 7: Update requirements.txt with Only Necessary Dependencies