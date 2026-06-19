import os

BOOKS_FILE = "books.txt"
ISSUED_FILE = "issued_books.txt"

# Each line in books.txt is stored as:  Title | Author | Status
# Status is either "Available" or "Issued"

# Each line in issued_books.txt is stored as: Title | Issued To


# ----------------------------- File Helpers ----------------------------- #

def ensure_files_exist():
    """Create the data files if they don't already exist."""
    if not os.path.exists(BOOKS_FILE):
        open(BOOKS_FILE, "w").close()
    if not os.path.exists(ISSUED_FILE):
        open(ISSUED_FILE, "w").close()


def load_books():
    """Read books.txt into a list of dicts: {title, author, status}."""
    books = []
    with open(BOOKS_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("|")
            if len(parts) == 3:
                title, author, status = parts
                books.append({
                    "title": title.strip(),
                    "author": author.strip(),
                    "status": status.strip()
                })
    return books


def save_books(books):
    """Write the full list of books back to books.txt."""
    with open(BOOKS_FILE, "w") as f:
        for book in books:
            f.write(f"{book['title']} | {book['author']} | {book['status']}\n")


def load_issued():
    """Read issued_books.txt into a list of dicts: {title, issued_to}."""
    issued = []
    with open(ISSUED_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("|")
            if len(parts) == 2:
                title, issued_to = parts
                issued.append({
                    "title": title.strip(),
                    "issued_to": issued_to.strip()
                })
    return issued


def save_issued(issued):
    """Write the full list of issued records back to issued_books.txt."""
    with open(ISSUED_FILE, "w") as f:
        for record in issued:
            f.write(f"{record['title']} | {record['issued_to']}\n")


# ----------------------------- Core Features ----------------------------- #

def add_book():
    """Allow the user to add a new book to the library."""
    print("\n--- Add Book ---")
    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()

    if not title or not author:
        print("Title and Author cannot be empty. Book not added.")
        return

    books = load_books()

    # Prevent exact duplicate entries
    for book in books:
        if book["title"].lower() == title.lower() and book["author"].lower() == author.lower():
            print("This book already exists in the library.")
            return

    books.append({"title": title, "author": author, "status": "Available"})
    save_books(books)
    print("Book Added Successfully!")


def view_books():
    """Display all books currently in the library."""
    print("\n--- Available Books ---")
    books = load_books()

    if not books:
        print("No books found in the library.")
        return

    print(f"{'Title':<30}{'Author':<25}{'Status':<10}")
    print("-" * 65)
    for book in books:
        print(f"{book['title']:<30}{book['author']:<25}{book['status']:<10}")


def search_book():
    """Search for books by title or author."""
    print("\n--- Search Book ---")
    query = input("Enter Title or Author to search: ").strip().lower()

    if not query:
        print("Search field cannot be empty.")
        return

    books = load_books()
    results = [
        b for b in books
        if query in b["title"].lower() or query in b["author"].lower()
    ]

    if not results:
        print("No matching books found.")
        return

    print(f"\nFound {len(results)} result(s):")
    print(f"{'Title':<30}{'Author':<25}{'Status':<10}")
    print("-" * 65)
    for book in results:
        print(f"{book['title']:<30}{book['author']:<25}{book['status']:<10}")


def issue_book():
    """Issue an available book to a user."""
    print("\n--- Issue Book ---")
    title = input("Enter Book Name to Issue: ").strip()

    books = load_books()
    found = None
    for book in books:
        if book["title"].lower() == title.lower():
            found = book
            break

    if not found:
        print("Book not found in the library.")
        return

    if found["status"] == "Issued":
        print("Sorry, this book is already issued to someone else.")
        return

    issued_to = input("Enter Your Name: ").strip()
    if not issued_to:
        print("Name cannot be empty. Book not issued.")
        return

    found["status"] = "Issued"
    save_books(books)

    issued = load_issued()
    issued.append({"title": found["title"], "issued_to": issued_to})
    save_issued(issued)

    print("Book Issued Successfully!")


def return_book():
    """Accept a returned book and mark it as available again."""
    print("\n--- Return Book ---")
    title = input("Enter Book Name to Return: ").strip()

    issued = load_issued()
    record = None
    for r in issued:
        if r["title"].lower() == title.lower():
            record = r
            break

    if not record:
        print("No record found of this book being issued.")
        return

    issued.remove(record)
    save_issued(issued)

    books = load_books()
    for book in books:
        if book["title"].lower() == title.lower():
            book["status"] = "Available"
            break
    save_books(books)

    print("Book Returned Successfully!")


# ------------------------------- Main Menu ------------------------------- #

def print_menu():
    print("\n========================================")
    print("   Welcome to Library Management System")
    print("========================================")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")


def main():
    ensure_files_exist()

    while True:
        print_menu()
        choice = input("Enter Choice: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            print("\nThank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
