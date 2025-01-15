class Book:
    def __init__(self, id, title, author, status="available"):
        self.id = id
        self.title = title
        self.author = author
        self.status = status

class LibrarySystem:
    def __init__(self):
        self.books = []
        self.users = []
        # Adding some sample books
        self.books.extend([
            Book(1, "The Great Gatsby", "F. Scott Fitzgerald"),
            Book(2, "To Kill a Mockingbird", "Harper Lee"),
            Book(3, "1984", "George Orwell")
        ])
    
    def add_book(self, title, author):
        new_id = len(self.books) + 1
        book = Book(new_id, title, author)
        self.books.append(book)
        return book
    
    def remove_book(self, book_id):
        self.books = [book for book in self.books if book.id != book_id]
    
    def search_book(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]
    
    def borrow_book(self, book_id):
        for book in self.books:
            if book.id == book_id and book.status == "available":
                book.status = "borrowed"
                return True
        return False
    
    def return_book(self, book_id):
        for book in self.books:
            if book.id == book_id and book.status == "borrowed":
                book.status = "available"
                return True
        return False 
