# Epic Title: Role-based Access Control

ALTER TABLE users
ADD COLUMN role_id INT NOT NULL,
ADD CONSTRAINT fk_role
FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE CASCADE;


# File 9: requirements.txt Update