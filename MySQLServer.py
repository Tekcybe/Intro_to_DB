import mysql.connector

def create_database():
    try:
        # Connect to MySQL server (update username/password)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="@Peter4Jesus"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error while connecting to MySQL: {err}")

    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
