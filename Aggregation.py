class Book:
    pass
class Library:
    def __init__(self, book):
        self.book = book
book = Book()
library = Library(book)
print(library.book)