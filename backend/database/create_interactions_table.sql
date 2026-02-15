# Epic Title: Interaction History and Documentation Upload

CREATE TABLE IF NOT EXISTS interactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    action VARCHAR(255) NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
);

# File 7: Update requirements.txt with Only Necessary Dependencies