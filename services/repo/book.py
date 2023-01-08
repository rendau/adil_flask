from domain.entity import book


class Book:
    def __init__(self, rr):
        self.rr = rr

    def list(self):
        self.rr.db.execute("""
            SELECT id, name, author, year
            FROM book
        """)

        return [book.Book(
            id=row[0],
            name=row[1],
            author=row[2],
            year=row[3]
        ) for row in self.rr.db.fetchall()]

    def get(self, id):
        self.rr.db.execute("""
            SELECT id, name, author, year
            FROM book
            WHERE id = ?
        """, (id,))

        row = self.rr.db.fetchone()

        return book.Book(
            id=row[0],
            name=row[1],
            author=row[2],
            year=row[3]
        )

    def create(self, data):
        self.rr.db.execute("""
            INSERT INTO book (name, author, year)
            VALUES (?, ?, ?)
        """, (data.name, data.author, data.year))

        self.rr.db.commit()

    def update(self, id, data):
        self.rr.db.execute("""
            UPDATE book
            SET name = ?, author = ?, year = ?
            WHERE id = ?
        """, (data.name, data.author, data.year, id))

        self.rr.db.commit()

    def delete(self, id):
        self.rr.db.execute("""
            DELETE FROM book
            WHERE id = ?
        """, (id,))

        self.rr.db.commit()
