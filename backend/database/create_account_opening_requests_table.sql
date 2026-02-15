# Epic Title: Streamline Account Opening Requests

CREATE TABLE IF NOT EXISTS account_opening_requests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    account_type VARCHAR(50) NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'Pending',
    submission_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    approved BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);


# File 6: Update app.py to Register Account Opening Request Blueprint