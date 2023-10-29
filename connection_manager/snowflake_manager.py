from utils.logger import get_logger
import snowflake.connector
class SnowflakeConnectionManager:
    def __init__(self, user, password, account, warehouse, database, schema):
        self.user = user
        self.password = password
        self.account = account
        self.warehouse = warehouse
        self.database = database
        self.schema = schema

        self.logger = get_logger()

    def connect(self):
        """
        Establish a connection to Snowflake.
        """
        try:
            self.logger.info("Connecting to Snowflake.")

            self.conn = snowflake.connector.connect(
                user=self.user,
                password=self.password,
                account=self.account,
                warehouse=self.warehouse,
                database=self.database,
                schema=self.schema
            )
            self.logger.info("Successfully connected to Snowflake.")
            return self.conn
        except Exception as e:
            self.logger.error(f"Error connecting to Snowflake: {str(e)}", exc_info=True)
            raise e

    def close(self, conn):
        """
        Close the connection to Snowflake.
        """
        if conn:
            try:
                conn.close()
                self.logger.info("Successfully closed the Snowflake connection.")
            except Exception as e:
                self.logger.error(f"Error while closing Snowflake connection: {str(e)}", exc_info=True)
                raise e
