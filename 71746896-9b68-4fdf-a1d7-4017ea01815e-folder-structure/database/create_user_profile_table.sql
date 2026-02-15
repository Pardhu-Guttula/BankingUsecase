-- Epic Title: Implement Multi-Factor Authentication

CREATE TABLE user_profile (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    phone_number VARCHAR(15),
    mfa_code INT,
    FOREIGN KEY (user_id) REFERENCES auth_user(id)
);