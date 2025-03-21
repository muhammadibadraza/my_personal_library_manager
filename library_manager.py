import json

LIBRARY_FILE = "library.json"
library = []  # Store books as a list

def load_library():
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_library(lib_data):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(lib_data, file, indent=4)

def add_book(library):
    title = input("Enter book title: ")
    author = input("Enter author: ")
    year = input("Enter publication year: ")
    genre = input("Enter genre: ")
    read_status = input("Have you read it? (yes/no): ").strip().lower()

    book = {"title": title, "author": author, "year": year, "genre": genre, "read": read_status}
    library.append(book)
    save_library(library)
    print("Book added successfully!\n")

def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            save_library(library)
            print("Book removed successfully!\n")
            return  # Exit function after removing book
    print("Book not found.\n")  # Will execute if book isn't found

def search_books(library):
    keyword = input("Enter title, author, or genre to search: ").lower()
    results = [book for book in library if keyword in book["title"].lower() or keyword in book["author"].lower() or keyword in book["genre"].lower()]

    if results:
        print("\nSearch Results:")
        for book in results:
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - Read: {book['read']}")
    else:
        print("No books found.")
    print()

def list_books(library):
    if not library:
        print("No books in library.\n")
        return
    print("\nYour Library:")
    for book in library:
        print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - Read: {book['read']}")
    print()

def show_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book['read'] == 'yes')
    unread_books = total_books - read_books
    genres = set(book['genre'] for book in library)

    print(f"\nLibrary Statistics:")
    print(f"Total Books: {total_books}")
    print(f"Books Read: {read_books}")
    print(f"Books Unread: {unread_books}")
    print(f"Genres in Collection: {', '.join(genres) if genres else 'None'}\n")

def main():
    global library
    library = load_library()

    while True:
        print("\nPersonal Library Manager")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display Statistics")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            list_books(library)
        elif choice == "5":
            show_statistics(library)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
