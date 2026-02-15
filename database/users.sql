# Epic Title: Create Secure User Sessions

CREATE TABLE users (
    id INT(11) NOT NULL AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(128) NOT NULL,
    is_active TINYINT(1) DEFAULT 1,
    mfa_enabled TINYINT(1) DEFAULT 0,
    PRIMARY KEY (id)
);



# File 7: Session Table SQL in database/sessions.sql