CREATE DATABASE user_registration;
USE user_registration;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(50) NOT NULL,
    mobile_number BIGINT(10) NOT NULL,
    password VARCHAR(255) NOT NULL
);
