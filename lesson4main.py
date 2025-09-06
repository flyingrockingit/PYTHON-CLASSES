class Library:
    def __init__(self, booklist, name):
        self.booklist = booklist
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"\n📚 Books available in {self.name} Library:")
        for book in self.booklist:
            print(f" - {book}")

    def lendBook(self, student_id, book):
        if book not in self.lendDict.keys():
            if book in self.booklist:
                self.lendDict.update({book: student_id})
                print(f"✅ Book '{book}' has been issued to Student ID: {student_id}")
            else:
                print(f"⚠️ Book '{book}' is not available in the library.")
        else:
            print(f"❌ Sorry, the book '{book}' is already lent to Student ID: {self.lendDict[book]}")

    def addBook(self, book):
        self.booklist.append(book)
        print(f"➕ Book '{book}' has been added to the library.")

    def returnBook(self, book):
        if book in self.lendDict.keys():
            self.lendDict.pop(book)
            print(f"📖 Book '{book}' has been returned successfully.")
        else:
            print(f"⚠️ The book '{book}' was not borrowed.")


if __name__ == "__main__":
    myLibrary = Library(
        ["Python Basics", "Data Science", "OOP in Java", "Machine Learning Handbook", "Deep Learning with Python", "Artificial Intelligence: A Modern Approach",
        "Database Management Systems", "Computer Networks", "Operating System Concepts",],
        "Murdoch"
    )

    while True:
        print(f"\n📖 Welcome to {myLibrary.name} Library! Choose a service:")
        print("1. Display books")
        print("2. Lend book")
        print("3. Add book")
        print("4. Return book")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            myLibrary.displayBooks()

        elif choice == "2":
            student_id = input("Enter your Student ID: ")
            book = input("Enter the book name you want to borrow: ")
            myLibrary.lendBook(student_id, book)

        elif choice == "3":
            book = input("Enter the name of the book to add: ")
            myLibrary.addBook(book)

        elif choice == "4":
            book = input("Enter the name of the book to return: ")
            myLibrary.returnBook(book)

        else:
            print("⚠️ Invalid choice. Please try again.")

    choice2 = input("\nEnter 'C' to continue or 'Q' to quit: ").lower()
    if choice2 == "q":
            print("👋 Thank you for visiting the library. Goodbye!")
    