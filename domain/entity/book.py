class Book:
    id: int
    name: str
    author: str
    year: int

    def __init__(self, id=None, name=None, author=None, year=None):
        self.id = id
        self.name = name
        self.author = author
        self.year = year
