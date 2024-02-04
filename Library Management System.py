class Book:
    def __init__(self, book_id, title, author, is_available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = is_available

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            availability = "Available" if book.is_available else "Not Available"
            print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Status: {availability}")

    def borrow_book(self, title):
        book = self.search_book(title)
        if book:
            if book.is_available:
                book.is_available = False
                print(f"You have successfully borrowed '{book.title}'.")
            else:
                print(f"Sorry, '{book.title}' is currently not available.")
        else:
            print("Book not found in the library.")

    def return_book(self, title):
        book = self.search_book(title)
        if book:
            if not book.is_available:
                book.is_available = True
                print(f"Thanks for returning '{book.title}'.")
            else:
                print("This book is already available in the library.")
        else:
            print("Book not found in the library.")

def main():
    library = Library()

    book1 = Book(1, "The Catcher in the Rye", "J.D. Salinger")
    book2 = Book(2, "To Kill a Mockingbird", "Harper Lee")
    book3 = Book(3, "1984", "George Orwell")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    library.display_books()

    library.borrow_book("The Catcher in the Rye")
    library.borrow_book("To Kill a Mockingbird")

    library.display_books()

    library.return_book("The Catcher in the Rye")

    library.display_books()

if __name__ == "__main__":
    main()
