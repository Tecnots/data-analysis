#  Data Analysis

This project connects to a MySQL database, reads data using SQLAlchemy, and performs data parsing and analysis such as date transformations and calculating differences.



## Configuration setup

To securely connect to your MySQL database, create a `.env` file in the project root and add your database credentials in the following format:

```env 

DB_USER='dbusername'
DB_PASSWORD='dbpassword'
DB_HOST='dbhost'
DB_PORT='dbport'
DB_NAME='dbname'

Change the values in singles quotes based on your database requirements