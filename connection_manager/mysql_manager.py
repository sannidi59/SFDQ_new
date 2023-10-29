import mysql.connector
from utils.logger import get_logger

class MySQLConnectionManager:
    def __init__(self, host, user, password, database, port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        self.logger = get_logger()

    def connect(self):
        """
        Establish a connection to the MySQL database.
        """
        try:
            self.logger.info("Connecting to MYSQL.")

            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.conn.is_connected():
                self.logger.info("Successfully connected to MySQL.")
                return self.conn
            else:
                raise Exception("Failed to connect to MySQL.")
        except Exception as e:
            self.logger.error(f"Error connecting to MySQL: {str(e)}", exc_info=True)
            raise e

    def close(self, conn):
        """
        Close the connection to the MySQL database.
        """
        if conn:
            try:
                conn.close()
                self.logger.info("Successfully closed the MySQL connection.")
            except Exception as e:
                self.logger.error(f"Error while closing MySQL connection: {str(e)}", exc_info=True)
                raise e
