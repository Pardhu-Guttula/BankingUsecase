# Epic Title: Core Banking System Integration

CREATE TABLE IF NOT EXISTS core_banking_transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT NOT NULL,
    amount FLOAT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (account_id) REFERENCES core_banking_accounts(id)
);


# File 10: Update requirements.txt with Only Necessary Dependencies