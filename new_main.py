import sys
import yaml
from connection_manager.snowflake_manager import SnowflakeConnectionManager
from connection_manager.mysql_manager import MySQLConnectionManager
from utils.credentials_handler import CredentialsHandler
from utils.comparisions import count_rows,compare_table_structures,compare_table_row_counts,get_table_structure
from utils.logger import get_logger

# Setup logger
logger = get_logger()

def load_tables_from_yaml(filename):
    """Load table names from a YAML file."""
    with open(filename, 'r') as file:
        tables = yaml.safe_load(file)
    return tables

def main():
    try:
        # Load tables from YAML
        tables = load_tables_from_yaml("tables.yaml")
        credentials = CredentialsHandler('config/config.ini')


        sf_manager = SnowflakeConnectionManager(**credentials.get_snowflake_credentials())
        sf_connection = sf_manager.connect()


        # MySQL connection and check
        mysql_manager = MySQLConnectionManager(**credentials.get_mysql_credentials())
        mysql_connection = mysql_manager.connect()

        # Assuming you want to compare tables one-by-one from the lists
        for s_table, m_table in zip(tables["snowflake"], tables["mysql"]):
            # Compare row counts
            snowflake_row_count = count_rows(s_table, sf_connection,"snowflake")
            mysql_row_count = count_rows(m_table, mysql_connection,"mysql")

            if compare_table_row_counts(snowflake_row_count, mysql_row_count):
                logger.info(f"Both {s_table} and {m_table} have the same number of rows: {snowflake_row_count}")
            else:
                logger.warning(f"{s_table} has {snowflake_row_count} rows while {m_table} has {mysql_row_count} rows")

            # Compare structures
            snowflake_structure = get_table_structure(s_table, sf_connection, "snowflake")
            mysql_structure = get_table_structure(m_table, mysql_connection, "mysql")

            if compare_table_structures(snowflake_structure, mysql_structure):
                logger.info(f"Both {s_table} and {m_table} have the same structure!")
            else:
                logger.warning(f"Differences found between {s_table} and {m_table} structures.")

    except Exception as e:
        logger.error(f"Error occurred: {str(e)}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
