# Epic Title: Overview of Financial Activities

CREATE TABLE IF NOT EXISTS financial_activities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    activity_type VARCHAR(50) NOT NULL,
    amount FLOAT NOT NULL,
    description VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);


# File 7: requirements.txt