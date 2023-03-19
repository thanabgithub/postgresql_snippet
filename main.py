import psycopg2

def postgresql_connection(func):
    """
    A decorator that connects to a PostgreSQL database and passes the connection object to the decorated function.

    Args:
        func (function): A function that takes a psycopg2.extensions.connection object and additional arguments.

    Returns:
        function: A wrapped function that connects to a PostgreSQL database and passes the connection object to the decorated function.

    """
    def wrapper(*args, **kwargs):
        database = "your_database_name"
        user = "your_username"
        password = "your_password"
        host = "your_host"
        port = "your_port_number"
        conn = None
        try:
            conn = psycopg2.connect(
                database=database,
                user=user,
                password=password,
                host=host,
                port=port
            )
            func(conn, *args, **kwargs)
        except psycopg2.Error as e:
            error_message = e.pgerror
            print(f"PostgreSQL Error: {error_message}")
        finally:
            if conn:
                conn.close()
    return wrapper

@postgresql_connection
def execute_query(conn, query):
    """
    Executes a PostgreSQL query using a connection object.

    Args:
        conn (psycopg2.extensions.connection): A connection to the PostgreSQL database.
        query (str): The SQL query to execute.

    Raises:
        psycopg2.Error: If an error occurs during the execution of the query.

    """
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
    except psycopg2.Error as e:
        error_message = e.pgerror
        print(f"PostgreSQL Error: {error_message}")


@postgresql_connection
def execute_query(conn, query):
    """
    Executes a PostgreSQL query using a connection object.

    Args:
        conn (psycopg2.extensions.connection): A connection to the PostgreSQL database.
        query (str): The SQL query to execute.

    Raises:
        psycopg2.Error: If an error occurs during the execution of the query.

    """
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
    except psycopg2.Error as e:
        error_message = e.pgerror
        print(f"PostgreSQL Error: {error_message}")

# Example usage
query = "SELECT * FROM my_table"
execute_query(query)



