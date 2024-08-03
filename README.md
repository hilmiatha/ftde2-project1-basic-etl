# ftde2-project1-basic-etl
### Basic ETL/Batch Processing - FTDE 2 Project 1

[Link to Looker Dashboard](https://lookerstudio.google.com/reporting/f0f6336a-4082-4f4c-a0c5-9d1dcaed6c3a)

### Project Description

This project aims to implement a basic ETL (Extract, Transform, Load) process for batch processing data. The goal is to extract data from a variety of sources, transform it into a desired format, and load it into a target destination.

### Technologies Used

- Python: The main programming language used for implementing the ETL process.
- Pandas: A powerful data manipulation library in Python used for data transformation.
- SQL: The language used for querying and manipulating data in the target destination.
- Looker: A data visualization and business intelligence platform used for creating dashboards and reports.
- psycopg2: A PostgreSQL adapter for Python, used for connecting to and interacting with PostgreSQL databases.
- sqlalchemy: A SQL toolkit and Object-Relational Mapping (ORM) library for Python, used for database abstraction and interaction.

### Project Structure

The project is organized as follows:

```
Project 1/
├── .gitignore
├── config.json
├── connection.py
├── main.py
├── query/
│   ├── dwh_design.sql
│   ├── query.sql
├── README.md
├── requirements.txt
```

- `README.md`: This file contains the project description and relevant information.
- `main.py`: The main script that orchestrates the ETL process.
- `connection.py`: A Python module that contains functions for establishing connections to the production and data warehouse databases.

### Usage

1. Clone the project repository.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Configure the necessary credentials and connection settings in the appropriate files.
4. Run the `main.py` script to start the ETL process.
5. Access the Looker dashboard using the provided link for data visualization and analysis.


### Configuration

To connect to the production database and the data warehouse database, you can create a `config.json` file in the project directory with the following structure:

```json
{
    "prod_db": {
        "host": "your_prod_db_host",
        "port": "your_prod_db_port",
        "database": "your_prod_db_name",
        "username": "your_prod_db_username",
        "password": "your_prod_db_password"
    },
    "dwh_db": {
        "host": "your_dwh_db_host",
        "port": "your_dwh_db_port",
        "database": "your_dwh_db_name",
        "username": "your_dwh_db_username",
        "password": "your_dwh_db_password"
    }
}
```

Make sure to replace the placeholders (`your_prod_db_host`, `your_prod_db_port`, etc.) with the actual connection details for your production and data warehouse databases.

You can then load this configuration in your Python scripts using a JSON parser and use the values to establish connections to the respective databases.

Remember to keep the `config.json` file secure and not include it in version control to protect sensitive information.
