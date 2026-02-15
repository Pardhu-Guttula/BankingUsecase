# Epic Title: Role-based Access Control

CREATE TABLE IF NOT EXISTS permissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    description VARCHAR(255),
    last_updated DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
);


# File 10: Schema for RolePermission Table in database/create_role_permissions_table.sql