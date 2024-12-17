import sqlite3

# Function to establish a connection to the database
def connect_to_db(db_name="app_database.db"):
    """
    Connects to the SQLite database specified by db_name.
    If the database does not exist, it will be created.
    
    :param db_name: The name of the database file.
    :return: A connection object to the SQLite database.
    """
    try:
        connection = sqlite3.connect(db_name)
        print(f"Connected to database: {db_name}")
        return connection
    except sqlite3.Error as e:
        print(f"An error occurred while connecting to the database: {e}")
        return None

# Function to close the database connection
def close_db_connection(connection):
    """
    Closes the connection to the SQLite database.
    
    :param connection: The connection object to the SQLite database.
    """
    try:
        if connection:
            connection.close()
            print("Database connection closed.")
    except sqlite3.Error as e:
        print(f"An error occurred while closing the database connection: {e}")