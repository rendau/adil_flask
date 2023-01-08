from flask import jsonify, request, Response
from domain.entity import book


class Book:
    def __init__(self, root):
        self.root = root

        self.set_routes()

    def set_routes(self):
        self.root.app.add_url_rule('/book', view_func=self.list)
        self.root.app.add_url_rule('/book/<id>', view_func=self.get)
        self.root.app.add_url_rule('/book', view_func=self.create, methods=['POST'])
        self.root.app.add_url_rule('/book/<id>', view_func=self.update, methods=['PUT'])
        self.root.app.add_url_rule('/book/<id>', view_func=self.delete, methods=['DELETE'])

    def list(self):
        items = self.root.core.book.list()
        return jsonify([x.__dict__ for x in items])

    def get(self, id):
        item = self.root.core.book.get(id)
        return jsonify(item.__dict__)

    def create(self):
        json = request.get_json()
        self.root.core.book.create(book.Book(**json))
        return Response(status=200)

    def update(self, id):
        json = request.get_json()
        self.root.core.book.update(id, book.Book(**json))
        return Response(status=200)

    def delete(self, id):
        self.root.core.book.delete(id)
        return Response(status=200)
