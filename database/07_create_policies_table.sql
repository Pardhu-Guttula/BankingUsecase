# Epic Title: Access Policies for Different Roles

CREATE TABLE policies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    role_id INT NOT NULL,
    resource VARCHAR(100) NOT NULL,
    can_view BOOLEAN DEFAULT FALSE NOT NULL,
    can_edit BOOLEAN DEFAULT FALSE NOT NULL,
    can_delete BOOLEAN DEFAULT FALSE NOT NULL,
    FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE CASCADE
);


# File 8: requirements.txt Update