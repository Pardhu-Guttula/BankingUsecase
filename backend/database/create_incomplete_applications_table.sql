# Epic Title: Interaction History and Documentation Upload

CREATE TABLE IF NOT EXISTS incomplete_applications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    form_data TEXT NOT NULL,
    saved_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

# File 7: Update requirements.txt with Required Dependency