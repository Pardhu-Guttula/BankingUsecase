# Epic Title: Develop a User-Friendly Dashboard

CREATE TABLE user_profiles (
    id INT(11) NOT NULL AUTO_INCREMENT,
    user_id INT(11) NOT NULL,
    display_name VARCHAR(100) NOT NULL,
    preferences VARCHAR(500),
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);



# File 8: Database Schema for Account in database/accounts.sql