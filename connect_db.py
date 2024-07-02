import mysql.connector
from mysql.connector import Error

def connect_db():
    db_name = "LMS_db"
    user = "root"
    password = "Lunaluna24!"
    host = "localhost"

    try:
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host
        )

        if conn.is_connected():
            print("Connected to mysql database successfully! ")
            return conn
    except Error as e:
        print(f"Error: {e}")
    
connect_db()














