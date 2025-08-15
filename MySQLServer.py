
import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (change user & password accordingly)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="@Peter4Jesus"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close cursor & connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
