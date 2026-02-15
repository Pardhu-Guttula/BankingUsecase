# Epic Title: User Authentication and Security

CREATE TABLE IF NOT EXISTS mfa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    secret VARCHAR(64) NOT NULL,
    confirmed BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);


# File 7: Update requirements.txt with Only Necessary Dependencies