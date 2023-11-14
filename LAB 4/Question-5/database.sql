-- Create a new database for user registration
CREATE DATABASE user_registration_ques4; 

-- Use the new database  
USE user_registration_ques4;

-- Create a table to store user information
CREATE TABLE usersques4 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(50) NOT NULL UNIQUE,
    mobile_number BIGINT(15) NOT NULL,
    password VARCHAR(255) NOT NULL
);