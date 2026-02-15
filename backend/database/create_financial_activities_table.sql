# Epic Title: Personalized Dashboard

CREATE TABLE IF NOT EXISTS financial_activities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    activity_type VARCHAR(50) NOT NULL,
    amount FLOAT NOT NULL,
    date DATETIME NOT NULL,
    description VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

# File 7: Update requirements.txt with Required Dependencies