import json
import os

DATA_FILE = "library_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return [
        {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "available": True},
        {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "available": True},
        {"id": 3, "title": "1984", "author": "George Orwell", "available": False}
    ]

def save_data(books):
    with open(DATA_FILE, "w") as file:
        json.dump(books, file, indent=4)

def display_books(books):
    print("\n--- Library Collection ---")
    if not books:
        print("No books available.")
        return
    for book in books:
        status = "Available" if book["available"] else "Borrowed"
        print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Status: {status}")

def add_book(books):
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    if title and author:
        new_id = max([b["id"] for b in books], default=0) + 1
        books.append({"id": new_id, "title": title, "author": author, "available": True})
        save_data(books)
        print(f"Success: '{title}' added to the library.")
    else:
        print("Error: Title and author cannot be empty.")

def borrow_book(books):
    display_books(books)
    try:
        book_id = int(input("\nEnter Book ID to borrow: "))
        for book in books:
            if book["id"] == book_id:
                if book["available"]:
                    book["available"] = False
                    save_data(books)
                    print(f"Success: You borrowed '{book['title']}'.")
                else:
                    print("Sorry, this book is currently borrowed.")
                return
        print("Error: Book ID not found.")
    except ValueError:
        print("Invalid input. Please enter a numerical ID.")

def return_book(books):
    try:
        book_id = int(input("\nEnter Book ID to return: "))
        for book in books:
            if book["id"] == book_id:
                if not book["available"]:
                    book["available"] = True
                    save_data(books)
                    print(f"Success: You returned '{book['title']}'.")
                else:
                    print("This book was not borrowed.")
                return
        print("Error: Book ID not found.")
    except ValueError:
        print("Invalid input. Please enter a numerical ID.")

def main():
    books = load_data()
    while True:
        print("\n==============================")
        print("  LIBRARY MANAGEMENT SYSTEM   ")
        print("==============================")
        print("1. View All Books")
        print("2. Add a New Book")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == "1":
            display_books(books)
        elif choice == "2":
            add_book(books)
        elif choice == "3":
            borrow_book(books)
        elif choice == "4":
            return_book(books)
        elif choice == "5":
            print("\nThank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()
              
