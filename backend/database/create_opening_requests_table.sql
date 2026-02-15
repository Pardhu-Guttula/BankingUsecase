# Epic Title: Account Opening and Service Modifications

CREATE TABLE IF NOT EXISTS opening_requests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    account_type VARCHAR(100) NOT NULL,
    status VARCHAR(50) DEFAULT 'pending' NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

# File 7: Update requirements.txt with Only Necessary Dependencies