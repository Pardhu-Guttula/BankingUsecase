# Epic Title: Account Opening and Service Modifications

CREATE TABLE IF NOT EXISTS approval_workflows (
    id INT AUTO_INCREMENT PRIMARY KEY,
    request_id INT NOT NULL,
    request_type VARCHAR(50) NOT NULL,
    submitted_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    approval_status VARCHAR(50) NOT NULL DEFAULT 'pending',
    approved_by INT,
    processed_date DATETIME,
    FOREIGN KEY (approved_by) REFERENCES users(id)
);

# File 7: Update requirements.txt with Required Dependency