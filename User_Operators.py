from Users import User
from connect_db import connect_db
from mysql.connector import Error
import re

def add_user(cursor):
    try:
        name = input("\nPlease Enter The Full Name:\n")
        if not re.fullmatch(r"[\w\s]+", name):
            print("\nInvalid Input. Please enter a valid name\n")
            return
        library_id = input("\nPlease Enter Six Digit Library ID #:\n")
        if not re.fullmatch(r"^\d{6}$", library_id):
            print("\nInvalid Type Error. Please Enter Valid Input\n")
            return
        new_user = User(name, library_id)
        query = "INSERT INTO Users (name, library_id) VALUES (%s, %s)"
        cursor.execute(query, (name, library_id))
        print(f"\nUser: {new_user.get_name()} with Library ID: {new_user.get_library_id()} has been added\n")
    except Error as e:
        print(f"Error: {e}")

def view_user(cursor):
    name = input("\nPlease Enter Full Name Of The User You're Searching For:\n")
    if not re.fullmatch(r"[\w\s]+", name):
        print("\nInvalid Input. Please enter a valid name\n")
        return
    query = "SELECT name, library_id FROM Users WHERE name = %s"
    cursor.execute(query, (name,))
    user = cursor.fetchone()
    if user:
        print(f"\nUser: {user[0]}\nLibrary ID: {user[1]}\n")
    else:
        print("\nUser not found\n")
        
def display_users(cursor):
    print("\nHere's The List Of Users On File:\n")
    query = "SELECT name, library_id FROM Users"
    cursor.execute(query)
    users = cursor.fetchall()
    for user in users:
        print(f"\nUser: {user[0]}\nLibrary ID: {user[1]}\n")

def users_main():
    continue_menu = True
    conn = connect_db()
    cursor = conn.cursor()
    while continue_menu:
        try:
            response = input("\nPlease Choose A Number From The Menu Below:\n1. Add User\n2. View User\n3. Display Users\n4. Menu\n")
            if response == "1":
                add_user(cursor)
                conn.commit()
            elif response == "2":
                view_user(cursor)
            elif response == "3":
                display_users(cursor)
            elif response == "4":
                break
            else:
                print("\nNot A Valid Input\n")
        except Exception as e:
            print(f"\nError: {e} Please Enter Valid Input\n")

    cursor.close()
    conn.close()


