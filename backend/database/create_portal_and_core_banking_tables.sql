# Epic Title: Core Banking System Integration

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(120) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    UNIQUE (username),
    UNIQUE (email)
);

CREATE TABLE IF NOT EXISTS core_banking_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT NOT NULL,
    balance FLOAT NOT NULL,
    status VARCHAR(50) NOT NULL,
    last_updated DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
);

# File 9: Update requirements.txt with Only Necessary Dependencies