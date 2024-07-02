class User:
    def __init__(self, name, library_id, borrowed_books=None):
        self.__name = name
        self.__library_id = library_id
        if borrowed_books is None:
            self.__borrowed_books = {}


    def get_name(self):
        return self.__name
    
    def get_library_id(self):
        return self.__library_id
    
    def get_borrowed_books(self):
        return self.__borrowed_books
