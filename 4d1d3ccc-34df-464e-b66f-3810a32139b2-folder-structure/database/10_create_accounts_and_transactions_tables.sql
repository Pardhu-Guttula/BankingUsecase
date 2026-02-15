# Epic Title: Develop a User-Friendly Dashboard

CREATE TABLE accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    account_number VARCHAR(20) UNIQUE NOT NULL,
    account_type VARCHAR(50) NOT NULL,
    balance FLOAT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT NOT NULL,
    amount FLOAT NOT NULL,
    transaction_type VARCHAR(50) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES accounts(id) ON DELETE CASCADE
);


# File 9: requirements.txt Update