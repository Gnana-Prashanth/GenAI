# Library Management System

A simple terminal-based Library Management System built in Python as part of the
THINK CHAMP PVT LTD internship mini project.

## Overview

This application helps a librarian manage books in a library. It runs entirely in
the terminal and lets users add books, view available books, search for books,
issue books, and return books. All data is automatically saved to text files so
records persist between runs.

## Features

- **Add Book** – Add a new book (title + author) to the library.
- **View Books** – Display all books currently in the library along with their status.
- **Search Book** – Search for books by title or author.
- **Issue Book** – Issue an available book to a user.
- **Return Book** – Return a previously issued book, making it available again.
- **File Storage** – Book and issue records are saved automatically to `.txt` files.
- **Menu-Driven Program** – A looping menu lets users repeat actions until they choose to exit.

## Project Structure

```
Library_Management_System/
│
├── library.py          # Main program
├── books.txt            # Stores book records (Title | Author | Status)
├── issued_books.txt     # Stores issued book records (Title | Issued To)
└── README.md             # This file
```

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Open a terminal in the `Library_Management_System` folder.
3. Run the program:

   ```bash
   python library.py
   ```

4. Follow the on-screen menu to add, view, search, issue, or return books.

## Sample Output

```
========================================
   Welcome to Library Management System
========================================
1. Add Book
2. View Books
3. Search Book
4. Issue Book
5. Return Book
6. Exit
Enter Choice: 1
Enter Book Title: Python Programming
Enter Author Name: John Smith
Book Added Successfully!
```

## Data File Format

**books.txt** — one book per line:
```
Title | Author | Status
```

**issued_books.txt** — one issued record per line:
```
Title | Issued To
```

## Possible Future Enhancements

- Book categories
- Student login system
- Due date management and fine calculation
- Book availability status badges
- Search by ISBN number
- Colored terminal output