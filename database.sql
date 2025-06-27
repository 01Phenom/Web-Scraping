CREATE DATABASE IF NOT EXISTS web_scraping_db;

USE web_scraping_db;

CREATE TABLE IF NOT EXISTS website_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(255) NOT NULL,
    meta_title VARCHAR(255),
    meta_description TEXT,
    social_media_links TEXT,
    tech_stack TEXT,
    payment_gateways TEXT
);
