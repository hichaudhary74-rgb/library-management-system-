# library-management-system-

# Overview of the Project

This project is a simple Python-based Library Management System that helps in maintaining basic records of books in a library.
The system works through a menu-driven console interface where the user can add new books, search for existing books, issue books, return them, and view the entire list of books stored in the library.

The main aim of this project is to provide an easy and efficient way of managing small library operations without using any database or advanced tools. It is beginner-friendly and focuses mainly on logic building through Python.

# Features

1. Add Book

The user can add a new book by entering details such as Book ID, Title, Author, and Number of Copies.
The system also checks if a book with the same ID already exists to prevent duplication.

2. Search Book

A book can be searched using its Book ID.
If found, the system displays complete details including available copies and issued copies.

3. Issue Book

The system allows issuing a book if copies are available.
It also keeps track of how many copies have been issued.

4. Return Book

The user can return a book that was previously issued.
The issued count is reduced accordingly.

5. Display All Books

All books stored in the library are shown with their complete details such as:

Title

Author

Total copies

Copies issued

Copies available

6. Exit

Close the program safely.
   
# Technologies/tools Used

Python 3

Console / Terminal for execution

Basic Python data structures (List and Dictionary)
No external libraries or database is used, which makes the project simple and easy for beginners.
6. Exit

Closes the program safely. 

# Stept o install & run the project

Installation

1. Install Python 3 from the official website.

2. Create a Python file named library.py.

3. Copy and paste the project code into the file.
 
 Running the Program

1. Open Command Prompt or Terminal.

2. Navigate to the folder where library.py is saved.

3. Run the program using:
python library.py

4. Follow the menu shown on the screen and enter your choices.

# Instructions for testing

To check whether the system works correctly, the following tests can be performed:

Test 1: Adding a Book

Enter:

Book ID

Title

Author

Quantity
The system should add the book successfully.


Test 2: Searching for a Book

Search using a valid Book ID.
The book details should appear.

Test 3: Issuing a Book

Issue a book that has available copies.
The "issued" count should increase.

Test 4: Returning a Book

Return a book that has been issued earlier.
