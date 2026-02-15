# Epic Title: Access Policies for Different Roles

CREATE TABLE IF NOT EXISTS policies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    role_id INT NOT NULL,
    service_name VARCHAR(255) NOT NULL,
    action VARCHAR(50) NOT NULL,
    FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE CASCADE
);


# File 6: Update `app.py` to Register Policy Controller