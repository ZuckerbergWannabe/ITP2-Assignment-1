# Library Management System

# Initialize the list of books
books = []

def display_menu():
    print("\nLibrary Management System")
    print("1. Add a Book")
    print("2. Search for a Book")
    print("3. Borrow a Book")
    print("4. Return a Book")
    print("5. View All Books")
    print("6. Exit")

def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()
    try:
        year = int(input("Enter publication year: "))
        if year <= 0:
            raise ValueError
    except ValueError:
        print("Year must be a positive integer.")
        return

    try:
        copies = int(input("Enter number of copies: "))
        if copies < 0:
            raise ValueError
    except ValueError:
        print("Copies must be a non-negative integer.")
        return

    # Check if the book already exists
    for book in books:
        if book['title'].lower() == title.lower():
            book['copies_available'] += copies
            print(f"Updated the number of copies for '{title}'.")
            return

    # Add a new book
    books.append({
        'title': title,
        'author': author,
        'year': year,
        'copies_available': copies
    })
    print(f"Added '{title}' to the library.")

def search_book():
    title = input("Enter the title of the book to search: ").strip()
    for book in books:
        if book['title'].lower() == title.lower():
            print(f"\nTitle: {book['title']}\nAuthor: {book['author']}\nYear: {book['year']}\nCopies Available: {book['copies_available']}")
            return
    print("The book was not found.")

def borrow_book():
    title = input("Enter the title of the book to borrow: ").strip()
    for book in books:
        if book['title'].lower() == title.lower():
            if book['copies_available'] > 0:
                book['copies_available'] -= 1
                print(f"Successfully borrowed '{title}'.")
            else:
                print(f"'{title}' is currently unavailable.")
            return
    print("The book was not found.")

def return_book():
    title = input("Enter the title of the book to return: ").strip()
    for book in books:
        if book['title'].lower() == title.lower():
            book['copies_available'] += 1
            print(f"Successfully returned '{title}'.")
            return
    print("The book was not found.")

def view_all_books():
    if not books:
        print("No books in the library.")
        return

    print(f"{'Title':<30}{'Author':<20}{'Year':<10}{'Copies':<10}")
    print("-" * 70)
    for book in books:
        print(f"{book['title']:<30}{book['author']:<20}{book['year']:<10}{book['copies_available']:<10}")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            add_book()
        elif choice == 2:
            search_book()
        elif choice == 3:
            borrow_book()
        elif choice == 4:
            return_book()
        elif choice == 5:
            view_all_books()
        elif choice == 6:
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
