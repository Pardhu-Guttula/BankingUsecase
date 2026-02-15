# Epic Title: Role-based Access Control

CREATE TABLE IF NOT EXISTS permissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    description VARCHAR(255)
);

# File 9: Schema for Role-Permission Association Table in database/create_role_permissions_table.sql