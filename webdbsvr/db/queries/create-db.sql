-- Create the database
CREATE DATABASE IF NOT EXISTS testdb;

-- Use the database
USE testdb;

-- Create the user_credentials table
CREATE TABLE IF NOT EXISTS user_credentials (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);

-- Create the user_info table
CREATE TABLE IF NOT EXISTS user_info (
    user_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    age INT,
    FOREIGN KEY (user_id) REFERENCES user_credentials(user_id) ON DELETE CASCADE
);

-- Insert sample data into user_credentials
INSERT INTO user_credentials (username, password) VALUES
('user1', 'password1'),
('user2', 'password2'),
('user3', 'password3'),
('user4', 'password4'),
('user5', 'password5');

-- Insert corresponding sample data into user_info
INSERT INTO user_info (user_id, name, email, age) VALUES
(1, 'Alice Smith', 'alice@example.com', 30),
(2, 'Bob Johnson', 'bob@example.com', 25),
(3, 'Carol Williams', 'carol@example.com', 28),
(4, 'David Brown', 'david@example.com', 35),
(5, 'Eve Davis', 'eve@example.com', 22);

