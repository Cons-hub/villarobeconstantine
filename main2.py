from book import Book
from queue_manager import BorrowingQueue


def main():
    borrowing_queue = BorrowingQueue()

    while True:
        print("\n==============================")
        print("   LIBRARY BORROWING SYSTEM")
        print("==============================")
        print("1. Add Borrowing Request")
        print("2. Process Next Request")
        print("3. Display All Pending Requests")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:

                book_id = int(input("Enter Book ID: "))
                title = input("Enter Book Title: ")
                borrower = input("Enter Borrower Name: ")

                book = Book(book_id, title, borrower)

                borrowing_queue.add_request(book)

            elif choice == 2:

                borrowing_queue.process_request()

            elif choice == 3:

                borrowing_queue.display_requests()

            elif choice == 4:

                print("\nProgram ended.")
                break

            else:

                print("\nInvalid choice. Please select 1-4.")

        except ValueError:

            print("\nInvalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()