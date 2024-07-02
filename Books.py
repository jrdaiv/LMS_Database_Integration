
class Book:
    def __init__(self, title, author, genre, publication_date, availability_status=True):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.is_available = availability_status


    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_genre(self):
        return self.__genre

    def get_publication_date(self):
        return self.__publication_date
    
    def get_availability_status(self):
        return "Available" if self.is_available else "Borrowed"
    
    def set_availability_status(self, status):
        self.is_available = status
    
    def get_borrow_book(self):
        if self.is_available:
            self.is_available = False
            return True
        return False
      
    def get_return_book(self):
        self.set_availability_status(True)
        return True

    def __str__(self):
        return f"{self.get_title()} by {self.get_author()} genre: {self.get_genre()} year published: {self.get_publication_date()} status: {self.get_availability_status()}"




