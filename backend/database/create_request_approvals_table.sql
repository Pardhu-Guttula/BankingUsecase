# Epic Title: Account Opening and Service Modifications

CREATE TABLE IF NOT EXISTS request_approvals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    request_id INT NOT NULL,
    request_type VARCHAR(50) NOT NULL,
    status VARCHAR(50) DEFAULT 'Pending' NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    approver_id INT,
    FOREIGN KEY (approver_id) REFERENCES users(id)
);


# File 10: Update requirements.txt with Only Necessary Dependencies