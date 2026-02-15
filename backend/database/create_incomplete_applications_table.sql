# Epic Title: Interaction History and Documentation Upload

CREATE TABLE IF NOT EXISTS incomplete_applications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    status VARCHAR(50) NOT NULL,
    application_data TEXT NOT NULL,
    saved_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
);

# File 7: Update requirements.txt with Only Necessary Dependencies