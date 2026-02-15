# Epic Title: Account Opening and Service Modifications

CREATE TABLE IF NOT EXISTS account_opening_requests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    account_type VARCHAR(50) NOT NULL,
    initial_deposit FLOAT NOT NULL,
    status VARCHAR(20) DEFAULT 'pending' NOT NULL,
    submitted_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);


# File 9: Update requirements.txt with Only Necessary Dependencies