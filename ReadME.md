# Web Scraping Solution

This is a Python script to scrape information from websites including meta title, 
meta description, social media links, tech stack, and payment gateways, and store the data into a MySQL database.

## Setup

1. **Install Dependencies**:
    ```
    pip install requests beautifulsoup4 mysql-connector-python
    ```

2. **MySQL Database Setup**:
    - Install MySQL Server if not already installed.
    - Execute the SQL script provided (`web_scraping_db.sql`) to create the necessary database and table.

3. **Configure MySQL Connection**:
    - Open `web_scraper.py` and update `your_username` and `your_password` with your MySQL username and password.

4. **Run the Script**:
    ```
    python web_scraper.py
    ```

## File Structure

- `web_scraper.py`: Python script to scrape websites and store data into MySQL.
- `web_scraping_db.sql`: SQL script to create the necessary tables in the MySQL database.

## Dependencies

- requests
- beautifulsoup4
- mysql-connector-python

#
