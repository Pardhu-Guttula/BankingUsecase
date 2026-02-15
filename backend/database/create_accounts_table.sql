# Epic Title: Personalized Dashboard

CREATE TABLE IF NOT EXISTS accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    account_number VARCHAR(20) UNIQUE NOT NULL,
    account_type VARCHAR(50) NOT NULL,
    balance INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);