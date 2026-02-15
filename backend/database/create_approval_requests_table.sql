# Epic Title: Account Opening and Service Modifications

CREATE TABLE IF NOT EXISTS approval_requests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    request_type VARCHAR(50) NOT NULL,
    request_id INT NOT NULL,
    status VARCHAR(20) DEFAULT 'pending' NOT NULL,
    submitted_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    reviewed_at DATETIME DEFAULT NULL,
    approved_by INT DEFAULT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (approved_by) REFERENCES users(id)
);


# File 8: Update requirements.txt with Only Necessary Dependencies