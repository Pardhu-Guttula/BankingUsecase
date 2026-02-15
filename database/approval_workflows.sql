# Epic Title: Approval and Processing Workflows

CREATE TABLE approval_workflows (
    id INT(11) NOT NULL AUTO_INCREMENT,
    request_id INT(11) NOT NULL,
    request_type VARCHAR(50) NOT NULL,
    status VARCHAR(20) DEFAULT 'pending',
    approver VARCHAR(50),
    PRIMARY KEY (id)
);


# File 7: Updated AccountRequest Schema in database/account_requests.sql