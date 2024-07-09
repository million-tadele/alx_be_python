# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def is_checked_out(self):
        return self._is_checked_out

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_checked_out():
                book.check_out()
                print(f"Checked out '{title}'.")
                return
        print(f"Book '{title}' is either not available or already checked out.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book.is_checked_out():
                book.return_book()
                print(f"Returned '{title}'.")
                return
        print(f"Book '{title}' is either not checked out or not in the library.")

    def list_available_books(self):
        print("Available books:")
        for book in self._books:
            if not book.is_checked_out():
                print(f"{book.title} by {book.author}")

# Checking for methods inside the Book class: check_out, return_book
if __name__ == "__main__":
    print("Checking for Methods inside the Book Class:")
    book = Book("Title", "Author")
    print(f"Check out method exists: {'check_out' in dir(book)}")
    print(f"Return book method exists: {'return_book' in dir(book)}")

    print("\nChecking for Methods inside the Library Class:")
    library = Library()
    print(f"Add book method exists: {'add_book' in dir(library)}")
    print(f"Check out book method exists: {'check_out_book' in dir(library)}")
    print(f"Return book method exists: {'return_book' in dir(library)}")
    print(f"List available books method exists: {'list_available_books' in dir(library)}")



# main.py

from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()
