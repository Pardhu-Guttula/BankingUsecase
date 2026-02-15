# Epic Title: User Authentication and Security

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    is_2fa_enabled BOOLEAN DEFAULT FALSE NOT NULL,
    encryption_key VARCHAR(44) NOT NULL,
    encrypted_credentials VARCHAR(255),
    last_updated DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
);


# File 6: Schema for User Security Table in database/create_user_security_table.sql