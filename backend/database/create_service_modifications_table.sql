# Epic Title: Account Opening and Service Modifications

CREATE TABLE IF NOT EXISTS service_modifications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    service_name VARCHAR(100) NOT NULL,
    action VARCHAR(50) NOT NULL,
    status VARCHAR(20) DEFAULT 'Pending' NOT NULL,
    request_date DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    approval_date DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(id)
);


# File 9: Update requirements.txt with Only Necessary Dependencies