# Epic Title: Maintain Separate Database

CREATE TABLE IF NOT EXISTS portal_main_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_key VARCHAR(255) NOT NULL,
    data_value VARCHAR(255) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);


# File 6: Update `app.py` to Register Portal Main Database Controller