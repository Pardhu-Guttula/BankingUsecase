# Epic Title: Save and Resume Incomplete Applications

CREATE TABLE IF NOT EXISTS incomplete_applications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    application_data TEXT NOT NULL,
    saved_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);


# File 6: Update `app.py` to Register Incomplete Application Blueprint