# Epic Title: Role-based Access Control

CREATE TABLE IF NOT EXISTS roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    description VARCHAR(255),
    last_updated DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
);


# File 8: Update requirements.txt with Only Necessary Dependencies