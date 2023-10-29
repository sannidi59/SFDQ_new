def count_rows(table_name, conn, database_type):
    """
    Count rows in a table.

    :param table_name: Name of the table.
    :param conn_manager: Instance of the connection manager (either Snowflake or MySQL).
    :param database_type: "snowflake" or "mysql".
    :return: Count of rows.
    """
    if database_type == "snowflake":
        query = f"SELECT COUNT(*) FROM {table_name}"
    elif database_type == "mysql":
        query = f"SELECT COUNT(*) FROM {table_name}"
    else:
        raise ValueError("Unsupported database type")

    cursor = conn.cursor()
    cursor.execute(query)
    count = cursor.fetchone()[0]
    cursor.close()
    return count

def get_table_structure(table_name, conn,database_type):
    """
    Get table structure (columns and types).

    :param table_name: Name of the table.
    :param conn_manager: Instance of the connection manager (either Snowflake or MySQL).
    :param database_type: "snowflake" or "mysql".
    :return: List of tuples with column names and types.
    """
    if database_type == "snowflake":
        query = f"DESCRIBE TABLE {table_name}"
    elif database_type == "mysql":
        query = f"DESCRIBE {table_name}"
    else:
        raise ValueError("Unsupported database type")

    cursor = conn.cursor()
    cursor.execute(query)
    columns = cursor.fetchall()
    print(columns)
    cursor.close()
    
    return [(col[0], col[1]) for col in columns]

def compare_table_structures(structure_snowflake, structure_mysql):
    """
    Compare the structures of two tables.

    :param structure_snowflake: Structure from Snowflake.
    :param structure_mysql: Structure from MySQL.
    :return: True if structures match, False otherwise.
    """
    return structure_snowflake == structure_mysql

def compare_table_row_counts(count_snowflake, count_mysql):
    """
    Compare row counts of two tables.

    :param count_snowflake: Row count from Snowflake.
    :param count_mysql: Row count from MySQL.
    :return: True if counts match, False otherwise.
    """
    return count_snowflake == count_mysql
