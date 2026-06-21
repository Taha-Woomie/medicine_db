import psycopg2
import config

def get_connection():
    """
    Returns a connection object to the database based on the credentials in config.py
    """
    return psycopg2.connect(
        host=config.DB_HOST,
        database=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASSWORD
    )
        
def execute_query(query, params=None):
    """
    Query helper for INSERT/DELETE/UPDATE, first argument is the raw string and second argument are any number
    of needed parameters. This helper handles exceptions and closing the connection
    and cursor after execution.
    """
    conn = None

    try:
        conn = get_connection()

        with conn.cursor() as cursor:
            cursor.execute(query, params)

        conn.commit()

    except psycopg2.Error as e:
        if conn:
            conn.rollback()

        print(f"Database error: {e}")
        raise

    finally:
        if conn:
            conn.close()

def execute_query_select(query, params=None, fetchall=True):
    """
    Query helper for SELECT, first argument is the raw string and second argument are any number
    of needed parameters, and finally fetchall is a switch for singular/multiple fetch. 
    This helper handles exceptions and closing the connection and cursor after execution.
    Returns a list of tuples of rows.
    """
    conn = None

    try:
        conn = get_connection()

        with conn.cursor() as cursor:
            cursor.execute(query, params)

            if fetchall:
                return cursor.fetchall()

            return cursor.fetchone()

    except psycopg2.Error as e:
        if conn:
            conn.rollback()

        raise

    finally:
        if conn:
            conn.close()