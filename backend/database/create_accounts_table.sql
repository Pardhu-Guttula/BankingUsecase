# Epic Title: Account Opening and Service Modifications

CREATE TABLE IF NOT EXISTS accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    account_number VARCHAR(20) UNIQUE NOT NULL,
    account_type VARCHAR(50) NOT NULL,
    balance INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);


# File 8: Create Schema for Account Opening Form Table in database/