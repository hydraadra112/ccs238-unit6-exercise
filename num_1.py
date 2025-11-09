# CARADO & TACUEL
# UNIT 6 EXERCISE

# Create a base/parent class called Book with class attributes
# like title, author, ISBN, and a method getDetails() that 
# returns book information.

# Apply proper encapsulation (getter/setter methods, public/private modifiers)
class Book:
    def __init__(self, title: str, author: str = '', isbn: str = ''):
        self._title = title
        self._author = author
        self._isbn = isbn
    
    # GETTERS & SETTERS
    @property
    def title(self) -> str:
        return self._title
    @title.setter
    def title(self, new_title: str) -> None:
        self._title = new_title

    @property
    def author(self) -> str:
        return self._author
    @author.setter
    def author(self, new_author:str) -> None:
        self._author = new_author

    @property
    def isbn(self) -> str:
        return self._isbn
    @isbn.setter
    def isbn(self, new_isbn:str) -> None:
        self._isbn = new_isbn
    
    def getDetails(self) -> dict:
        # Uses the getter methods to return the value
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn
        }

# PrintedBook (with an additional attribute such as number of pages)
# Create two derived classes
class PrintedBook(Book):
    def __init__(self, title: str, author: str = '', isbn: str = '',
                 pages: int = 0):
        super().__init__(title, author, isbn)
        self._pages = pages
    
    @property
    def pages(self) -> int:
        return self._pages
    @pages.setter
    def pages(self, new_num_pages : int) -> None:
        self._pages = new_num_pages 
    
    def getDetails(self) -> dict:
        details = super().getDetails()
        details.update({'pages': self.pages})
        return details

# EBook (with attributes such as file format and file size)
class EBook(Book):
    def __init__(self, title: str, author: str = '', isbn: str = '',
                 size_megabytes: int = 15, file_format: str = 'txt',):
        super().__init__(title, author, isbn)
        self._size_megabytes = size_megabytes
        self._file_format = file_format
    
    @property
    def size(self) -> int:
        return self._size_megabytes
    @size.setter
    def size(self, new_size: int) -> None:
        self._size_megabytes = new_size

    @property
    def format(self) -> str:
        return self._file_format
    @format.setter
    def format(self, new_format: str) -> None:
        self._file_format = new_format
    
    def getDetails(self) -> dict:
        details = super().getDetails()
        details.update({
            'mb_size': self.size,
            'format': self.format
        })
        return details

if __name__ == '__main__':
    # Create an array containing 1 Book, 1 PrintedBook, and 1 EBook.
    # Then create a loop that will call each instance’s getDetails() method.
    # Attach a screenshot of the console output.

    books = [Book('Harry Potter',
                  'JK Rowling',
                  '123-456-789'),

            PrintedBook('Cujo',
                        'Stephen Hawking', 
                        '456-789-123',
                        600 # Pages
                        ),

            EBook('1984',
                  'George Orwell',
                  '789-456-123',
                  25, # Size in MB
                  'pdf' # File format
                  )
                  ]
    
    for book in books:
        book_type = book.__class__.__name__
        book_details = book.getDetails()
        print(f"{book_type}:")
        
        for key, val in book_details.items():
            print(f"\t{key}: {val}")


# Ref
# https://www.geeksforgeeks.org/python/method-resolution-order-in-python-inheritance/
# https://www.geeksforgeeks.org/python/getter-and-setter-in-python/