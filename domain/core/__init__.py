from .book import Book


class Core:
    def __init__(self, repo):
        self.repo = repo

        self.book = Book(self)
