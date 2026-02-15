# Epic Title: Personalized Dashboard

CREATE TABLE IF NOT EXISTS widgets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    widget_type VARCHAR(255) NOT NULL,
    position INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);


# File 7: Update requirements.txt with Only Necessary Dependencies