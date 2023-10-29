import pytest
from utils.credentials_handler import CredentialsHandler
from connection_manager.snowflake_manager import SnowflakeConnectionManager
from connection_manager.mysql_manager import MySQLConnectionManager



def test_snowflake_connection(snowflake_conn):
    """Test establishing a connection to Snowflake using the fixture."""
    assert snowflake_conn is not None, "Snowflake connection failed."

def test_mysql_connection(mysql_conn):
    """Test establishing a connection to MySQL using the fixture."""
    assert mysql_conn is not None, "MySQL connection failed."

def test_snowflake_invalid_credentials():
    """Test Snowflake connection with invalid credentials."""
    invalid_credentials = {
        "user": "invalid_user",
        "password": "invalid_pass",
        "account": "invalid_account"
    }
    with pytest.raises(Exception):  # replace with a more specific exception if applicable
        sf_manager = SnowflakeConnectionManager(invalid_credentials)
        conn = sf_manager.connect()

def test_mysql_invalid_credentials():
    """Test MySQL connection with invalid credentials."""
    invalid_credentials = {
        "user": "invalid_user",
        "password": "invalid_pass",
        "host": "invalid_host",
        "port": 1234,
        "database": "invalid_db"
    }
    with pytest.raises(Exception):  # replace with a more specific exception if applicable
        mysql_manager = MySQLConnectionManager(invalid_credentials)
        conn = mysql_manager.connect()

def test_snowflake_query(snowflake_conn):
    """Test querying data from Snowflake."""
    cursor = snowflake_conn.cursor()
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    assert result[0] == 1

def test_mysql_query(mysql_conn):
    """Test querying data from MySQL."""
    cursor = mysql_conn.cursor()
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    assert result[0] == 1

# def fetch_data_from_snowflake(table_name):
#     with snowflake_manager.connect() as conn:
#         cursor = conn.cursor()
#         query = f"SELECT * FROM {table_name}"
#         cursor.execute(query)
#         return cursor.fetchall()
#
# def fetch_data_from_mysql(table_name):
#     with mysql_manager.connect() as conn:
#         cursor = conn.cursor()
#         query = f"SELECT * FROM {table_name}"
#         cursor.execute(query)
#         return cursor.fetchall()
#
# tables = read_tables_from_yaml()
#
# @pytest.mark.parametrize("table_name", tables['tables'])
# def test_data_comparison(table_name):
#
#     snowflake_data = fetch_data_from_snowflake(table_name)
#     mysql_data = fetch_data_from_mysql(table_name)
#
#     result = compare_data(snowflake_data, mysql_data)
#
#     assert result == True, f"Data mismatch between Snowflake and MySQL for table {table_name}"
