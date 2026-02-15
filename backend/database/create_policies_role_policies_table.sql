# Epic Title: Role-based Access Control

CREATE TABLE IF NOT EXISTS policies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description VARCHAR(255) NULL
);

CREATE TABLE IF NOT EXISTS role_policies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    role_id INT NOT NULL,
    policy_id INT NOT NULL,
    FOREIGN KEY (role_id) REFERENCES roles(id),
    FOREIGN KEY (policy_id) REFERENCES policies(id)
);

# File 9: Update requirements.txt with Only Necessary Dependencies