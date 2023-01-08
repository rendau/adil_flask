from domain.core import Core
from services.db.sqlite import Db
from services.repo import Repo
from services.server.rest.flask import Server


class App:
    def start(self):
        self.db = Db('./data/db.sqlite3')

        self.repo = Repo(self.db)

        self.core = Core(self.repo)

        self.server = Server(self.core)

        self.server.run(port=9090, debug=True)


if __name__ == "__main__":
    app = App()

    # Start the app
    app.start()
