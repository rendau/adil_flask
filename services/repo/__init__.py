from .book import Book


class Repo:
    def __init__(self, db):
        self.db = db

        self.book = Book(self)
