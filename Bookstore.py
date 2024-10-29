class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def borrow(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Checked Out"
        return f'"{self.title}" by {self.author} ({status})'


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True
        return False

    def __str__(self):
        return f"User ID: {self.user_id}, Name: {self.name}"


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def view_all_books(self):
        return "\n".join(f"{i+1}. {str(book)}" for i, book in enumerate(self.books))

    def search_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def view_all_users(self):
        return "\n".join(str(user) for user in self.users)


library = Library()
library.add_book(Book(1, "To Kill a Mockingbird", "Harper Lee"))
library.add_book(Book(2, "1984", "George Orwell", False))
library.add_book(Book(3, "The Great Gatsby", "F. Scott Fitzgerald"))
library.add_user(User(1, "Alice"))

while True:
    print("Welcome to the Community Library System!")
    print("----------------------------------------")
    print("Please choose an option:")
    print("1. View all books")
    print("2. Search for a book")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. View all users")
    print("6. Exit")
    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        print("\nAll Books:")
        print(library.view_all_books())
        print("----------------------------------------")
    elif choice == 2:
        book_id = int(input("Enter the Book ID to search: "))
        book = library.search_book(book_id)
        if book:
            print(book)
        else:
            print("Book not found.")
    elif choice == 3:
        user_id = int(input("Enter your User ID: "))
        book_id = int(input("Enter the Book ID you want to borrow: "))
        user = next((u for u in library.users if u.user_id == user_id), None)
        book = library.search_book(book_id)
        if user and book:
            if user.borrow_book(book):
                print(f'You have borrowed "{book.title}".')
            else:
                print(f'Sorry, the book "{book.title}" is currently checked out.')
        else:
            print("Invalid User ID or Book ID.")
        print("----------------------------------------")
    elif choice == 4:
        user_id = int(input("Enter your User ID: "))
        book_id = int(input("Enter the Book ID you want to return: "))
        user = next((u for u in library.users if u.user_id == user_id), None)
        book = library.search_book(book_id)
        if user and book:
            if user.return_book(book):
                print(f'You have returned "{book.title}".')
            else:
                print("You did not borrow this book.")
        else:
            print("Invalid User ID or Book ID.")
    elif choice == 5:
        print("\nAll Users:")
        print(library.view_all_users())
        print("----------------------------------------")
    elif choice == 6:
        break
    else:
        print("Invalid choice. Please try again.")
