import unittest

class Book():

    title: str 
    author: str
    isbn: str
    available: bool

    def __init__(self, title, author, isbn, available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __str__(self):
        return self.title

    def borrow_book(self):
        if(self.available):
            self.available = False
        else:
            pass

    def return_book(self):
        if(self.available):
            print("Error: Book is already checked in.")
        else:
            print("Book successfully returned")
            self.available = True
            
class User():
    
    name: str
    user_id: str
    borrowed_books: list

    def __init__(self, name, user_id, borrowed_books):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = borrowed_books

    def borrow_book(self, book):
        if(book.available):
            self.borrowed_books.append(book)
            print(self.user_id + ": " + self.name + " --- succesfully checked out " + book.title)
        else:
            print(self.user_id + ": " + self.name + " --- unable to check out " + book.title + ". Book unavailable")

    def return_book(self, book):
        self.borrowed_books.remove(book)
        print(self.user_id + ": " + self.name + " --- succesfully returned " + book.title)

    def view_borrowed_books(self):
        for book in self.borrowed_books:
            print(book.title)

class Library():

    books: list
    users: list

    def __init__(self, books, users):
        self.books = books
        self.users = users

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def borrow_book(self, user, book):
        user.borrow_book(book)
        book.borrow_book()

    def return_book(self, user, book):
        user.return_book(book)
        book.return_book()

    def list_available_books(self):
        for book in self.books:
            if(book.available):
                print(book.title + ": Available")
            else:
                pass

# ----------
# Unit Tests
# ----------

class TestBook(unittest.TestCase):

    # Test object creation
    def test_create(self):
        book1 = Book("Book", "Author", "ISBN-0000", True)
        self.assertEqual(book1.title, "Book")
        self.assertEqual(book1.author, "Author")
        self.assertEqual(book1.isbn, "ISBN-0000")
        self.assertEqual(book1.available, True)
        print("\n")

    # Test book being unavailable after borrow.
    def test_borrow(self):
        book1 = Book("Book", "Author", "ISBN-0000", True)
        book1.borrow_book()
        self.assertEqual(book1.available, False)
        print("\n")

    # Test book being available after borrowing and then returning.
    def test_return(self):
        book1 = Book("Book", "Author", "ISBN-0000", True)
        book1.borrow_book()
        book1.return_book()
        self.assertEqual(book1.available, True)
        print("\n")

class TestUser(unittest.TestCase):

    # Test book object is in the user's list.
    def test_borrow(self):
        book1 = Book("Book", "Author", "ISBN-0000", True)
        user1 = User("name", "01", list())
        user1.borrow_book(book1)
        print(user1.borrowed_books)
        print("\n")

    # Test object is no longer in list.
    def test_return(self):
        book1 = Book("Book", "Author", "ISBN-0000", True)
        user1 = User("name", "01", list())
        user1.borrow_book(book1)
        user1.return_book(book1)
        print(user1.borrowed_books)
        print("\n")

    # Test the view method shows book titles instead of objects' memory locations.
    def test_view(self):
        book1 = Book("Book", "Author", "ISBN-0000", True)
        book2 = Book("Dune", "Frank Herbert", "ISBN-1234", True)
        user1 = User("name", "01", list())
        user1.borrow_book(book1)
        user1.borrow_book(book2)
        user1.view_borrowed_books()
        print("\n")

class TestLibrary(unittest.TestCase):
    
    # Test book object is in the library's list after adding.
    def test_addBook(self):
        library1 = Library(list(), list())
        book1 = Book("Book", "Author", "ISBN-0000", True)
        library1.add_book(book1)
        print(library1.books)
        print("\n")

    # Test book oject is no longer in list after removing.
    def test_removeBook(self):
        library1 = Library(list(), list())
        book1 = Book("Book", "Author", "ISBN-0000", True)
        library1.add_book(book1)
        library1.remove_book(book1)
        print(library1.books)
        print("\n")

    # Test user object in the library's list after adding.
    def test_addUser(self):
        library1 = Library(list(), list())
        user1 = User("name", "01", list())
        library1.add_user(user1)
        print(library1.users)
        print("\n")

    # Test book object is no longer in list after removing.
    def test_removeUser(self):
        library1 = Library(list(), list())
        user1 = User("name", "01", list())
        library1.add_user(user1)
        library1.remove_user(user1)
        print(library1.users)
        print("\n")

    # Test logic works where the library object can interact with the Book and User objects.
    def test_borrow(self):
        library1 = Library(list(), list())
        user1 = User("name", "01", list())
        book1 = Book("Book", "Author", "ISBN-0000", True)
        library1.borrow_book(user1, book1)
        print("\n")

    # Test logic works where the library object can interact with the Book and User objects.
    def test_return(self):
        library1 = Library(list(), list())
        user1 = User("name", "01", list())
        book1 = Book("Book", "Author", "ISBN-0000", True)
        library1.borrow_book(user1, book1)
        library1.return_book(user1, book1)
        print("\n")