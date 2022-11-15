# ***************************************
# Imports
# ***************************************
import pandas as pd
from sqlalchemy import create_engine, exc
import configparser

# ***************************************
# Import af datamodel Mysql
# ***************************************

# MySQL connection
def connect():
    db_conn = None
    try:
        # Read config.ini file
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Connect to MySQL
        db_connection_str = config['mysqlini']['conn_string']
        db_conn = create_engine(db_connection_str)
        
        return db_conn

    except exc.SQLAlchemyError as e:
        print(e)

    finally:
        db_conn.dispose() # Close connection


# EmployeesSale
def get_data():
    conn = connect()
    EmployeesSale = pd.read_sql('SELECT * FROM EmployeesSale', conn)
    return EmployeesSale

def get_year():
    # Year - Opret dataframe med år
    conn = connect()
    df_year = pd.read_sql('SELECT DISTINCT order_year FROM EmployeesSale;', conn)

    return df_year