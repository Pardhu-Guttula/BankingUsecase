# Epic Title: Customizable Widgets

CREATE TABLE widgets (
    id INT(11) NOT NULL AUTO_INCREMENT,
    user_id INT(11) NOT NULL,
    widget_type VARCHAR(50) NOT NULL,
    settings VARCHAR(255),
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);



# File 6: Updated User Schema for Widget Relationships in database/users.sql