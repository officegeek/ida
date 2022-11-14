# Imports
from numpy import product
import pandas as pd
from sqlalchemy import create_engine, exc
import configparser

# MySQL forbindelsen
def connect():
    db_conn = None
    try:
        # Læs config.ini filen
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Opret forbindelse til MySQL
        db_connection_str = config['mysql']['conn_string']
        db_conn = create_engine(db_connection_str)
    
        return db_conn

    except exc.SQLAlchemyError as e:
        print(e)

    finally:
        db_conn.dispose() # Luk forbindelsen

# Employees
def get_employees():
    conn = connect()
    df_Employees = pd.read_sql('SELECT EmployeeID, FirstName, LastName FROM employees;', conn)
    return df_Employees

# Product sales
def get_product_sales():
    conn = connect()
    df_Product_Sale = pd.read_sql('SELECT * FROM Products_Sale;', conn)
    return df_Product_Sale
