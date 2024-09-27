"""
This script connects to a MySQL database and stores some emails and hashed
passwords in the database.
"""
import mysql.connector
import bcrypt

USERS_AND_PASSWORDS = (
    (1, "user1@example.com", "password1"),
    (2, "user2@example.com", "password2"),
)


def get_connection():
    """Connect to the database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='sales_db',
            user='root',
            password='Kusu!123'
        )
        return connection
    except mysql.connector.Error as err:
        raise Exception(f"Error connecting to the database: {err}")


def main():
    query = """
        INSERT INTO users(id, email, password) VALUES (%s, %s, %s)
    """
    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        for credential in USERS_AND_PASSWORDS:
            hashed_password = bcrypt.hashpw(credential[2].encode('utf-8'), bcrypt.gensalt())
            cursor.execute(query, (credential[0], credential[1], hashed_password))
        connection.commit()
        return {
            "status": "success",
            "message": "Records inserted successfully."
        }
    except Exception as ex:
        return {
            "message": "Something went wrong.",
            "detail": str(ex),
            "status": False
        }
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


if __name__ == "__main__":
    print(main())
