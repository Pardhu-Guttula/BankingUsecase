# Epic Title: Personalized Dashboard

CREATE TABLE IF NOT EXISTS account_dashboards (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    account_number VARCHAR(20) NOT NULL UNIQUE,
    account_type VARCHAR(50) NOT NULL,
    balance FLOAT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

# File 7: Update requirements.txt with Required Dependencies