# Epic Title: Streamline Account Opening Requests

CREATE TABLE account_requests (
    id INT(11) NOT NULL AUTO_INCREMENT,
    user_id INT(11) NOT NULL,
    account_type VARCHAR(50) NOT NULL,
    status VARCHAR(20) DEFAULT 'pending',
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);



# File 6: Updated User Schema in database/users.sql