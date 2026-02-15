-- Epic Title: Role-Based Access Control

CREATE TABLE role (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE permission (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE role_permissions (
    role_id INT NOT NULL,
    permission_id INT NOT NULL,
    FOREIGN KEY (role_id) REFERENCES role(id),
    FOREIGN KEY (permission_id) REFERENCES permission(id)
);

CREATE TABLE user_roles (
    user_id INT NOT NULL,
    role_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES auth_user(id),
    FOREIGN KEY (role_id) REFERENCES role(id)
);