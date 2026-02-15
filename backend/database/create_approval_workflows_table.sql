# Epic Title: Approval and Processing Workflows

CREATE TABLE IF NOT EXISTS approval_workflows (
    id INT AUTO_INCREMENT PRIMARY KEY,
    request_id INT NOT NULL,
    request_type VARCHAR(50) NOT NULL,
    approver_id INT NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'Pending',
    approval_date DATETIME,
    comments VARCHAR(255),
    FOREIGN KEY (approver_id) REFERENCES users(id) ON DELETE CASCADE
);


# File 6: Update app.py to Register Approval Workflow Blueprint