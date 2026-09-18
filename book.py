class Book:
    def __init__(self, book_id, title, borrower):
        self.book_id = book_id
        self.title = title
        self.borrower = borrower

    def display(self):
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Borrower: {self.borrower}")