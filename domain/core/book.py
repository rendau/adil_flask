from domain.entity.book import Book


class Book:
    def __init__(self, root):
        self.root = root

    def list(self):
        return self.root.repo.book.list()

    def get(self, id):
        return self.root.repo.book.get(id)

    def create(self, data):
        return self.root.repo.book.create(data)

    def update(self, id, data):
        return self.root.repo.book.update(id, data)

    def delete(self, id):
        return self.root.repo.book.delete(id)
