import configparser

class CredentialsHandler:
    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get_snowflake_credentials(self):
        """Fetch Snowflake database credentials."""
        try:
            return {
                "user": self.config.get("SNOWFLAKE", "USER"),
                "password": self.config.get("SNOWFLAKE", "PASSWORD"),
                "account": self.config.get("SNOWFLAKE", "ACCOUNT"),
                "warehouse": self.config.get("SNOWFLAKE", "WAREHOUSE"),
                "database": self.config.get("SNOWFLAKE", "DATABASE"),
                "schema": self.config.get("SNOWFLAKE", "SCHEMA")
            }
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            raise Exception(f"Error reading Snowflake credentials: {str(e)}")

    def get_mysql_credentials(self):
        """Fetch MySQL database credentials."""
        try:
            return {
                "host": self.config.get("MYSQL", "HOST"),
                "user": self.config.get("MYSQL", "USER"),
                "password": self.config.get("MYSQL", "PASSWORD"),
                "database": self.config.get("MYSQL", "DATABASE"),
                "port": self.config.getint("MYSQL", "PORT")
            }
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            raise Exception(f"Error reading MySQL credentials: {str(e)}")

