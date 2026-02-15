# Epic Title: Personalized Dashboard

CREATE TABLE IF NOT EXISTS financial_summaries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    total_balance FLOAT NOT NULL,
    total_transactions INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);


# File 7: Update requirements.txt with Only Necessary Dependencies