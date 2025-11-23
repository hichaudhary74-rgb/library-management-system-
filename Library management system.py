books = []

def add_book():
    print("\n--- Add New Book ---")
    book_id = input("Enter Book ID: ")

    for b in books:
        if b["id"] == book_id:
            print("Book with this ID already exists!")
            return

    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    quantity = int(input("Enter Number of Copies: "))

    book_data = {
        "id": book_id,
        "title": title,
        "author": author,
        "quantity": quantity,
        "issued": 0
    }

    books.append(book_data)
    print("Book added successfully!")


def search_book():
    print("\n--- Search Book ---")
    book_id = input("Enter Book ID to search: ")

    for b in books:
        if b["id"] == book_id:
            print("\nBook Found!")
            print("Title:", b["title"])
            print("Author:", b["author"])
            print("Available:", b["quantity"] - b["issued"])
            print("Issued:", b["issued"])
            return
    
    print("Book not found!")


def issue_book():
    print("\n--- Issue Book ---")
    book_id = input("Enter Book ID: ")

    for b in books:
        if b["id"] == book_id:
            available = b["quantity"] - b["issued"]

            if available > 0:
                b["issued"] += 1
                print("Book issued successfully!")
            else:
                print("No copies available!")
            return
    
    print("Book not found!")


def return_book():
    print("\n--- Return Book ---")
    book_id = input("Enter Book ID: ")

    for b in books:
        if b["id"] == book_id:
            if b["issued"] > 0:
                b["issued"] -= 1
                print("Book returned successfully!")
            else:
                print("No issued copy to return!")
            return
    
    print("Book not found!")


def display_all():
    if not books:
        print("No books available in the library!")
        return

    print("\n--- Library Books List ---")
    for b in books:
        print("\nBook ID:", b["id"])
        print("Title:", b["title"])
        print("Author:", b["author"])
        print("Total Copies:", b["quantity"])
        print("Issued:", b["issued"])
        print("Available:", b["quantity"] - b["issued"])


def main():
    while True:
        print("\n===============================")
        print("      LIBRARY MANAGEMENT")
        print("===============================")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Display All Books")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            search_book()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            display_all()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")


main()
