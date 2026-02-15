# Epic Title: Personalized Dashboard

CREATE TABLE IF NOT EXISTS widgets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    widget_type VARCHAR(50) NOT NULL,
    widget_data VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(id)
);


# File 9: Update requirements.txt with Only Necessary Dependencies