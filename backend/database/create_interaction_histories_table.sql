# Epic Title: Interaction History and Documentation Upload

CREATE TABLE IF NOT EXISTS interaction_histories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    action VARCHAR(255) NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);


# File 8: Update requirements.txt with Only Necessary Dependencies