# Epic Title: Personalized Dashboard

CREATE TABLE IF NOT EXISTS widgets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    name VARCHAR(50) NOT NULL,
    position INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

# File 7: Update requirements.txt with Required Dependencies