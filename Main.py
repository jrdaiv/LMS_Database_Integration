import Author_Operators
import Book_Operators
import User_Operators

  

def main():
    while True:
        try:
            response = input("\nPlease Choose From The Menu Below:\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit\n")
            if response == "1":
                Book_Operators.books_main()            
            elif response == "2":
                User_Operators.users_main()
            elif response == "3":
                Author_Operators.authors_main()
            elif response == "4":
                print("\nExiting Program...\n\nBeep..Boop..Bop...\n\nShutting Down Now..\n\nGoodbye!\n")
                break
            else:
                print("\nSorry Wrong Input\n")
        except Exception as e:
            print(f"\nError: {e} Please Type Correct Input\n")

if __name__ == "__main__":
    main()

