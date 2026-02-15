# Epic Title: Save and Resume Incomplete Applications

CREATE TABLE applications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    data TEXT NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'incomplete',
    save_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);


# File 8: requirements.txt Update