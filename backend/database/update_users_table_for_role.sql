# Epic Title: Role-based Access Control

ALTER TABLE users
ADD COLUMN role_id INT,
ADD CONSTRAINT fk_role
    FOREIGN KEY (role_id) 
    REFERENCES roles(id);

# File 10: Update requirements.txt with Required Dependencies