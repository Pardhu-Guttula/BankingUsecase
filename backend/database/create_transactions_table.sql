# Epic Title: Personalized Dashboard

CREATE TABLE IF NOT EXISTS transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT NOT NULL,
    amount INT NOT NULL,
    type VARCHAR(50) NOT NULL,
    date DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    description VARCHAR(255),
    FOREIGN KEY (account_id) REFERENCES accounts(id)
);


# File 9: Update requirements.txt with Only Necessary Dependencies