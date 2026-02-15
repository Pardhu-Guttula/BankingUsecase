# Epic Title: Core Banking System Integration

CREATE TABLE IF NOT EXISTS core_banking_accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_number VARCHAR(20) UNIQUE NOT NULL,
    balance FLOAT NOT NULL,
    last_synced DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);


# File 9: Schema for Core Banking Transaction Table in database/create_core_banking_transactions_table.sql