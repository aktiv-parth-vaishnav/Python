class Book:
    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.available = True

    def display_info(self):
        status = "Available" if self.available else "Checked Out"
        print(f"{self.title} by {self.author} (ISBN: {self.isbn}, Year: {self.year}) - {status}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn, year):
        new_book = Book(title, author, isbn, year)
        self.books.append(new_book)
        print(f"Book '{title}' added to the library.")

    def checkout_book(self, title):
        """
        this method allow user to check out books from
        library

        """
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                print(f"You checked out '{book.title}'.")
                return
        print(f"Book '{title}' is not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                print(f"You returned '{book.title}'.")
                return
        print(f"Book '{title}' was not borrowed or not found.")

    def search_books(self, keyword):
        """
        this method search books based on title of books
        and autor if keyword match in title either book
        print that book record
        """
        results = [book for book in self.books if
                   keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
        if results:
            print("Search Results:")
            for book in results:
                book.display_info()
        else:
            print(f"No books found for keyword '{keyword}'.")

    def list_available_books(self):

        available_books = [book for book in self.books if book.available]
        if available_books:
            print("Available Books:")
            for book in available_books:
                book.display_info()
        else:
            print("No books are currently available.")

    def display_book_info(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.display_info()
                return
        print(f"Book '{title}' not found.")


def library_system():
    library = Library()

    while True:
        print("\nLibrary Menu")
        print("1. Add Book")
        print("2. Checkout Book")
        print("3. Return Book")
        print("4. Search Books")
        print("5. List Available Books")
        print("6. Display Book Info")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            year = input("Enter publication year: ")
            library.add_book(title, author, isbn, year)

        elif choice == "2":
            title = input("Enter the book title to checkout: ")
            library.checkout_book(title)

        elif choice == "3":
            title = input("Enter the book title to return: ")
            library.return_book(title)

        elif choice == "4":
            keyword = input("Enter keyword (title/author) to search: ")
            library.search_books(keyword)

        elif choice == "5":
            library.list_available_books()

        elif choice == "6":
            title = input("Enter the book title to view info: ")
            library.display_book_info(title)

        elif choice == "7":
            print("Exiting Library System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Result output
library_system()
