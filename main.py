from connection_manager.snowflake_manager import SnowflakeConnectionManager
from connection_manager.mysql_manager import MySQLConnectionManager
from utils.logger import get_logger
from utils.credentials_handler import CredentialsHandler

logger = get_logger()


def main():
    try:
        # Initialize the CredentialsHandler
        logger.info("Reading creds from ini")
        credentials = CredentialsHandler('config/config.ini')

        # Snowflake connection and check
        sf_manager = SnowflakeConnectionManager(**credentials.get_snowflake_credentials())
        sf_connection = sf_manager.connect()


        # MySQL connection and check
        mysql_manager = MySQLConnectionManager(**credentials.get_mysql_credentials())
        mysql_connection = mysql_manager.connect()

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
    
    finally:
        sf_manager.close(sf_connection)
        mysql_manager.close(mysql_connection)



if __name__ == "__main__":
    main()
