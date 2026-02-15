# Epic Title: Manage Secure Storage of Credentials

CREATE TABLE users (
    id INT(11) NOT NULL AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(128) NOT NULL,
    is_active TINYINT(1) DEFAULT 1,
    mfa_enabled TINYINT(1) DEFAULT 0,
    PRIMARY KEY (id)
);



# File 6: Database Schema Update for Secure Storage in database/sessions.sql