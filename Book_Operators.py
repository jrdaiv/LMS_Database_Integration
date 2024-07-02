from Books import Book
from connect_db import connect_db
from mysql.connector import Error
import re

def add_book(cursor):
    try:
        title = input("\nPlease Enter The Title's Name, Press Enter To Skip:\n")
        if not re.fullmatch(r"[\w\s]+", title):
            print("\nInvalid Type Error. Please Enter Valid Input\n")
            return
        author_id = input("\nPlease Enter The Author's Name, Press Enter To Skip:\n")
        if not re.fullmatch(r"[\w\s]+", author_id):
            print("\nInvalid Type Error. Please Enter Valid Input\n")
            return
        genre_id = input("\nPlease Enter The Genre Name, Press Enter To Skip:\n")
        if not re.fullmatch(r"[\w\s]+", genre_id):
            print("\nInvalid Type Error. Please Enter Valid Input\n")
            return
        publication_date = input("\nPlease Enter The Date (xxxx-xx-xx) It Was Published, Press Enter To Skip:\n")
        if not re.fullmatch(r"^\d{4}-\d{2}-\d{2}$", publication_date):
            print("\nInvalid Type Error. Please Enter Valid Input\n")
            return
        book = Book(title, author_id, genre_id, publication_date, True)
        query = "INSERT INTO Books (title, author, genre, publication_date, availability) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (title, author_id, genre_id, publication_date, book.is_available))
        print(f"\nTitle:\n{book} Has Been Added Successfully To The Library\n")
        
    except Error as e:
        print(f"Error: {e}")

def check_out(cursor):
    try:
        title = input("\nPlease Enter The Book You'd Like To Borrow:\n")
        if not re.fullmatch(r"[\w\s]+", title):
            print("\nInvalid Type Error. Please Enter Valid Input\n")
            return
        library_id = input("\nPlease Enter Your Six Digit Library ID #\n")
        if not re.fullmatch(r"^\d{6}$", library_id):
            print("\nInvalid Type Error. Please Enter Valid Input\n")
            return
        query = "UPDATE Books SET availability = 0 WHERE title = %s AND availability = 1"
        cursor.execute(query, (title,))
        if cursor.rowcount > 0:
            print(f"\nBook: {title} Has Been Officially Been Checked Out To {library_id}\n")
        else:
            print("\nSorry, That Book Is Not Available\n")
    except Error as e:
        print(f"Error: {e}")

# need to fix
def return_book(cursor):
    try:
        title = input("\nPlease Enter The Book Title You're Returning:\n")
        if not re.fullmatch(r"[\w\s]+", title):
            print("\nInvalid Type Error. Please Enter Valid Input\n")
            return
        query = "UPDATE Books SET availability = 0 WHERE title = %s AND availability = 1"
        cursor.execute(query, (title,))
        if cursor.rowcount > 0:
            print(f"\nBook: {title} Has Been Officially Returned\n")
        else:
            print("\nSorry, That Book Was Not Checked Out\n")
    except Error as e:
        print(f"Error: {e}")

# need to fix
def search_book(cursor):
    try:
        title = input("\nPlease Enter The Name Of The Book You're Searching For:\n")
        if not re.fullmatch(r"[\w\s]+", title):
            print("\nInvalid Type Error. Please Enter Valid Input\n")
            return
        query = "SELECT title, author, genre, publication_date, availability FROM Books WHERE title = %s"
        cursor.execute(query, (title,))
        book = cursor.fetchone()
        if book:
            print(f"\nTitle: {book[0]}\nAuthor: {book[1]}\nGenre: {book[2]}\nPublished: {book[3]}\nStatus: {'Available' if book[4] else 'Checked Out'}\n")
        else:
            print("\nSorry, That Book Is Not In The Library:\n")
    except Error as e:
        print(f"Error: {e}")

# need to fix
def display_books(cursor):
    print("\nHere are The Books We Have In The Library:\n")
    query = "SELECT title, author, genre, publication_date, availability FROM Books"
    cursor.execute(query)
    books = cursor.fetchall()
    for book in books:
        print(f"\nTitle:\n{book[1]}\nAuthor: {book[1]}\nGenre: {book[2]}\nPublished: {book[3]}\nStatus: {'Available' if book[4] else 'Checked Out'}\n")
    
def books_main():
    continue_menu = True
    conn = connect_db()
    cursor = conn.cursor()
    while continue_menu:
        try:
            response = input("\nPlease Choose A Number From The List Below:\n1. Add New Book\n2. Borrow Book\n3. Return Book\n4. Search Book\n5. Display Books\n6. Menu\n")
            if response == "1":
                add_book(cursor)
                conn.commit()
            elif response == "2":
                check_out(cursor)
                conn.commit()
            elif response == "3":
                return_book(cursor)
                conn.commit()
            elif response == "4":
                search_book(cursor)
            elif response == "5":
                display_books(cursor)
            elif response == "6":
                break
            else:
                print("\nPlease Enter Valid Input\n")    

        except Exception as e:
            print(f"\nError: {e} Please Enter A Valid Input\n")

    cursor.close()
    conn.close()

