-- Epic Title: Approval and Processing Workflows

CREATE TABLE approval_workflows (
    id INT AUTO_INCREMENT PRIMARY KEY,
    request_id INT NOT NULL,
    request_type VARCHAR(50) NOT NULL,
    status VARCHAR(20) DEFAULT 'pending',
    processed_at TIMESTAMP NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);