import pytest
from connection_manager.snowflake_manager import SnowflakeConnectionManager
from connection_manager.mysql_manager import MySQLConnectionManager
from utils.credentials_handler import CredentialsHandler
from utils.logger import get_logger


# Fixture for Snowflake connection
@pytest.fixture(scope="module")
def snowflake_conn():
    """Provide a Snowflake connection to tests."""
    credentials = CredentialsHandler('..\config\config.ini')
    sf_manager = SnowflakeConnectionManager(**credentials.get_snowflake_credentials())
    sf_connection = sf_manager.connect()
    yield sf_connection  # This is the connection object that will be passed to tests
    sf_connection.close()  # Cleanup after tests are done


# Fixture for MySQL connection
@pytest.fixture(scope="module")
def mysql_conn():
    """Provide a MySQL connection to tests."""
    credentials = CredentialsHandler('..\config\config.ini')
    mysql_manager = MySQLConnectionManager(**credentials.get_mysql_credentials())
    mysql_connection = mysql_manager.connect()
    yield mysql_connection  # This is the connection object that will be passed to tests
    mysql_connection.close()  # Cleanup after tests are done
