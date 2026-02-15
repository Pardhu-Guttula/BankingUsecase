# Epic Title: Approval and Processing Workflows

CREATE TABLE approval_workflows (
    id INT AUTO_INCREMENT PRIMARY KEY,
    request_type VARCHAR(50) NOT NULL,
    request_id INT NOT NULL,
    approver_id INT NOT NULL,
    status VARCHAR(50) DEFAULT 'pending' NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (approver_id) REFERENCES users(id) ON DELETE CASCADE
);


# File 7: requirements.txt Update