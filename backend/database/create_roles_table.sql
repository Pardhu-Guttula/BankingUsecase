# Epic Title: Role-based Access Control

CREATE TABLE IF NOT EXISTS roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    description VARCHAR(255)
);

# File 9: Schema for Users Table Updated for Role in database/update_users_table_for_role.sql