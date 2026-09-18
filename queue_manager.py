from collections import deque


class BorrowingQueue:
    def __init__(self):
        self.queue = deque()

    def add_request(self, book):
        self.queue.append(book)
        print("\nBorrowing request added.")

    def process_request(self):
        if not self.queue:
            print("\nNo pending requests.")
            return

        book = self.queue.popleft()

        print("\n===== PROCESSING REQUEST =====")
        book.display()

    def display_requests(self):
        if not self.queue:
            print("\nNo pending requests.")
            return

        print("\n===== PENDING REQUESTS =====")

        for book in self.queue:
            print(
                f"Book ID: {book.book_id} | "
                f"Title: {book.title} | "
                f"Borrower: {book.borrower}"
            )