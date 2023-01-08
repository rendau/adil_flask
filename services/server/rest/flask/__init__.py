from flask import Flask

from .book import Book


class Server:
    def __init__(self, core):
        self.core = core

        self.app = Flask('app')

        Book(self)

    def run(self, host='0.0.0.0', port=9000, debug=False):
        self.app.run(host=host, port=port, debug=debug)
