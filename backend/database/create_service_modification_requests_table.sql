# Epic Title: Service Modification Requests

CREATE TABLE IF NOT EXISTS service_modification_requests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    account_id INT NOT NULL,
    modified_service VARCHAR(100) NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'Pending',
    submission_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    approved BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (account_id) REFERENCES accounts(id) ON DELETE CASCADE
);


# File 6: Update app.py to Register Service Modification Request Blueprint