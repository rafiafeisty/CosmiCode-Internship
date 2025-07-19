import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class library:
    def __init__(self):
        self.books = ["chronicles of narnia", "percy jackson", "silent patient", "girl on train"]
        self.borrowed = []

    def details(self):
        print("--------------------")
        print("Available books:")
        for book in self.books:
            print(book)
        print("\n")
        print("Borrowed Books:")
        for book in self.borrowed:
            print(book)
        print("--------------------")

    def add_book(self):
        self.books.append(input("Enter the name of the book: "))
        print("Book added successfully")

    def borrow_book(self):
        borrow = input("Enter the name of the book you want to borrow: ")
        if borrow in self.books:
            self.borrowed.append(borrow)
            self.books.remove(borrow)
            print("Book borrowed successfully")
        else:
            print("Book not found in available books.")

    def return_book(self):
        return_book = input("Enter the name of the book you want to return: ")
        if return_book in self.borrowed:
            self.borrowed.remove(return_book)
            self.books.append(return_book)
            print("Book returned successfully")
        else:
            print("This book is not in the borrowed list.")

    def delete_book(self):
        delete_book = input("Enter the name of the book you want to delete: ")
        if delete_book in self.books:
            self.books.remove(delete_book)
            print("Book deleted successfully")
        else:
            print("Book not found in the library.")

def menu(l1):
    while True:
        clear_screen()
        print("---------------------------------------------")
        print("1. Display details of library")
        print("2. Add a book to the library")
        print("3. Borrow a book from the library")
        print("4. Return a book to the library")
        print("5. Delete a book from the library")
        print("6. Exit")
        print("---------------------------------------------")
        choice = input("Enter your choice: ")

        clear_screen()

        if choice == "1":
            l1.details()
        elif choice == "2":
            l1.add_book()
        elif choice == "3":
            l1.borrow_book()
        elif choice == "4":
            l1.return_book()
        elif choice == "5":
            l1.delete_book()
        elif choice == "6":
            print("Thank you for using the library system.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

        input("\nPress Enter to continue...") 

l1 = library()
menu(l1)
