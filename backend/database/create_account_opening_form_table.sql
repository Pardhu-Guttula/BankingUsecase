# Epic Title: Account Opening and Service Modifications

CREATE TABLE IF NOT EXISTS account_opening_forms (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INT NOT NULL,
    initial_deposit INT NOT NULL
);


# File 9: Update requirements.txt with Only Necessary Dependencies