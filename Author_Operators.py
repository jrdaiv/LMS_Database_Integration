from Authors import Author
from connect_db import connect_db
from mysql.connector import Error
import re

def add_author(cursor):
    try:
        name = input("\nPlease Enter The Author's Full Name:\n")
        if not re.fullmatch(r"[\w\s]+", name):
            print("\nInvalid Input. Please enter a valid name\n")
            return
        bio = input("\nPlease Enter The Author's Biography:\n")
        author = Author(name, bio)
        query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
        cursor.execute(query, (author.get_name(), author.get_biography()))
    except Error as e:
        print(f"\nError:\n{e} Please input a valid input\n")

def view_author(cursor):
    try:
        name = input("\nPlease Enter The Full Name Of The Author You Would Like To Look Up:\n")
        if not re.fullmatch(r"[\w\s]+", name):
            print("Invalid Input. Please enter a valid name.")
            return
        query = "SELECT * FROM authors WHERE name = %s"
        cursor.execute(query, (name,))
        author = cursor.fetchone()
        if author:
            print(f"\nAuthor: {author[1]}\nBio: {author[2]}\n")
        else:
            print(f"\n{name} Not Found\n")
    except Error as e:
        print(f"Error: {e}")

def display_authors(cursor):
    print("\nHere Is The List Of Authors Currently In The Library\n")
    try:
        cursor.execute("SELECT * FROM authors")
        authors = cursor.fetchall()
        if authors:
            print("\nList of Authors:")
            for author in authors:
                print(f"\nName: {author[1]}\nBio: {author[2]}\n")
        else:
            print("\nNo authors found\n")
    except Error as e:
        print(f"Error: {e}")

def authors_main():
    conn = connect_db()
    cursor = conn.cursor()
    continue_menu = True
    while continue_menu:
        try:
            response = input("\nPlease Choose A Number From Menu Below:\n1. Add Author\n2. View Author\n3. Display Author's\n4. Menu\n")
            if response == "1":
                add_author(cursor)
                conn.commit()
            elif response == "2":
                view_author(cursor)
            elif response == "3":
                display_authors(cursor)
            elif response == "4":
                break
            else:
                print("Invalid Input\n")
        except Exception as e:
            print(f"Error:\n{e}\n")

    cursor.close()
    conn.close()