# Epic Title: Develop Secure APIs

CREATE TABLE IF NOT EXISTS core_banking_transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_id VARCHAR(255) NOT NULL UNIQUE,
    amount INT NOT NULL,
    transaction_type VARCHAR(50) NOT NULL,
    status VARCHAR(50) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);


# File 6: Update `app.py` to Register Core Banking Integration Controller