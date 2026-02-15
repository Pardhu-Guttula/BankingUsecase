# Epic Title: Personalized Dashboard

CREATE TABLE IF NOT EXISTS accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    account_number VARCHAR(20) UNIQUE NOT NULL,
    balance DECIMAL(10, 2) NOT NULL,
    account_type VARCHAR(20) NOT NULL,
    last_updated DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);


# File 9: Schema for Transaction Table in database/create_transactions_table.sql (Existing File, Re-emitting for Context)