class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def display_info(self):
        status = "Available" if self.is_available else "Borrowed"
        print(f"[{self.book_id}] {self.title} by {self.author} - {status}")


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is not available")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} does not have this book")


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' added successfully")

    def show_books(self):
        print(f"\nBooks in {self.name}:")
        for book in self.books:
            book.display_info()


# ---------------- MAIN PROGRAM ----------------

# Create library
library = Library("City Library")

# Create books
book1 = Book(1, "Python Basics", "John Smith")
book2 = Book(2, "OOP in Python", "David Warner")

# Add books to library
library.add_book(book1)
library.add_book(book2)

# Create member
member1 = Member(101, "Rahul")

# Add member
library.add_member(member1)

# Display books
library.show_books()

# Borrow a book
member1.borrow_book(book1)

# Display books after borrowing
library.show_books()

# Return the book
member1.return_book(book1)

# Display books after returning
library.show_books()