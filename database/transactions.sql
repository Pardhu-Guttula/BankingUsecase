# Epic Title: Develop a User-Friendly Dashboard

CREATE TABLE transactions (
    id INT(11) NOT NULL AUTO_INCREMENT,
    account_id INT(11) NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    transaction_type VARCHAR(30) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (account_id) REFERENCES accounts(id) ON DELETE CASCADE
);



# File 10: Update User Schema for Associations in database/users.sql