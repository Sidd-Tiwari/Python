class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
    
    def display_books(self):
        if not self.books:
            print("No books available in the library.")
            return
        
        print("\nLibrary Catalog:")
        for book in self.books:
            availability = "Available" if book.available else "Checked Out"
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Status: {availability}")
    
    def search_book(self, title):
        for book in self.books:
            if title.lower() in book.title.lower():
                availability = "Available" if book.available else "Checked Out"
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Status: {availability}")
                return
        print(f"Book '{title}' not found in the library.")
    
    def check_out_book(self, title):
        for book in self.books:
            if title.lower() in book.title.lower():
                if book.available:
                    book.available = False
                    print(f"You have checked out '{book.title}'.")
                else:
                    print(f"'{book.title}' is already checked out.")
                return
        print(f"Book '{title}' not found in the library.")
    
    def return_book(self, title):
        for book in self.books:
            if title.lower() in book.title.lower():
                if not book.available:
                    book.available = True
                    print(f"You have returned '{book.title}'. Thank you!")
                else:
                    print(f"'{book.title}' is already in the library.")
                return
        print(f"Book '{title}' not found in the library.")

def main():
    library = Library()
    
    while True:
        print("\nLibrary Management System")
        print("1. Add a Book")
        print("2. Display Books")
        print("3. Search for a Book")
        print("4. Check Out a Book")
        print("5. Return a Book")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            isbn = input("Enter the ISBN of the book: ")
            library.add_book(title, author, isbn)
            print(f"'{title}' has been added to the library.")
        
        elif choice == "2":
            library.display_books()
        
        elif choice == "3":
            title = input("Enter the title of the book to search: ")
            library.search_book(title)
        
        elif choice == "4":
            title = input("Enter the title of the book to check out: ")
            library.check_out_book(title)
        
        elif choice == "5":
            title = input("Enter the title of the book to return: ")
            library.return_book(title)
        
        elif choice == "6":
            print("Exiting the Library Management System.")
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
